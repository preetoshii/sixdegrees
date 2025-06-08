# --- ai_client.py ---

import os
import json
import config

# TODO: Make sure you have the 'openai' package installed (`pip install openai`).
# TODO: Make sure you have the 'python-dotenv' package installed (`pip install python-dotenv`).
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

def _load_prompt(filepath):
    """Loads a prompt from a text file."""
    try:
        with open(filepath, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: Prompt file not found at {filepath}")
        return None

# Initialize the OpenAI client
# The client automatically looks for the OPENAI_API_KEY environment variable.
try:
    client = OpenAI(timeout=config.AI_REQUEST_TIMEOUT)
except Exception as e:
    print(f"Error initializing OpenAI client: {e}")
    client = None

def find_connections(target_word, candidate_words):
    """
    Calls the AI to find the most related words for a target word.
    """
    if not client:
        print("AI client not initialized. Returning random sample.")
        import random
        return random.sample(candidate_words, min(config.NUM_CONNECTIONS, len(candidate_words)))

    prompt_template = _load_prompt(config.PROMPT_FOR_LINKS_FILE)
    if not prompt_template:
        return []

    system_prompt = prompt_template.format(num_connections=config.NUM_CONNECTIONS)
    
    user_prompt = f"""
    TARGET_WORD:
    "{target_word}"

    CANDIDATE_WORDS:
    {json.dumps(candidate_words)}
    """

    try:
        response = client.chat.completions.create(
            model=config.MODEL_FOR_LINKS,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            response_format={"type": "json_object"}
        )
        response_data = json.loads(response.choices[0].message.content)
        return response_data.get("connections", [])
    except Exception as e:
        print(f"Error calling AI for '{target_word}' connections: {e}")
        return []

def generate_description(target_word, required_connections):
    """
    Calls the AI to generate a wiki-style description for a target word.
    """
    if not client:
        print("AI client not initialized. Returning placeholder description.")
        return f"This is a placeholder description for '{target_word}' that would include: {', '.join(required_connections)}."

    system_prompt = _load_prompt(config.PROMPT_FOR_DESCRIPTIONS_FILE)
    if not system_prompt:
        return f"Error: Could not load description prompt for {target_word}."
    
    user_prompt = f"""
    TARGET_WORD:
    "{target_word}"

    REQUIRED_WORDS:
    {json.dumps(required_connections)}
    """
    
    try:
        response = client.chat.completions.create(
            model=config.MODEL_FOR_DESCRIPTIONS,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            response_format={"type": "json_object"},
            temperature=config.AI_TEMPERATURE
        )
        response_data = json.loads(response.choices[0].message.content)
        return response_data.get("description", "Error: Could not generate description.")
    except Exception as e:
        print(f"Error calling AI for '{target_word}' description: {e}")
        return f"Error generating description for {target_word}." 