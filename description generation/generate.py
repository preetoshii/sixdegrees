#!/usr/bin/env python3

"""
Description Generation System

This script handles the AI-powered generation of connections and descriptions for the game's words.
It uses OpenAI's API to:
1. Find meaningful connections between words
2. Generate wiki-style descriptions incorporating those connections
"""

import json
import time
import sys
import os
from typing import List, Dict, Any
from openai import OpenAI
from dotenv import load_dotenv

# Get the absolute path to the project's root directory
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Construct the absolute path to the .env file
dotenv_path = os.path.join(project_root, '.env')

# Load the .env file from the explicit path
load_dotenv(dotenv_path=dotenv_path)

# Debug: print the API key to verify it's loaded (mask most of it for security)
api_key = os.environ.get('OPENAI_API_KEY')
print(f"OPENAI_API_KEY loaded: {api_key[:8]}...{api_key[-4:] if api_key else 'Not Found'}")

# Add parent directory to path to import config and utils
sys.path.append(project_root)
from config import (
    WORDS_FILE,
    OUTPUT_GRAPH_FILE,
    NUM_CONNECTIONS,
    AI_TEMPERATURE,
    AI_REQUEST_TIMEOUT,
    MODEL_FOR_LINKS,
    MODEL_FOR_DESCRIPTIONS,
    SECONDS_BETWEEN_API_CALLS,
    FIND_CONNECTIONS_PROMPT,
    GENERATE_DESCRIPTION_PROMPT
)
from utils import save_word_graph

# ============================================================================
# AI API INTERACTION
# ============================================================================

# Instantiate OpenAI client
client = OpenAI()

def load_prompt(file_path: str) -> str:
    """Load a prompt from a file."""
    with open(file_path, 'r') as f:
        return f.read().strip()

def find_connections(
    word: str,
    all_words: List[str],
    num_connections: int,
    model: str,
    temperature: float,
    timeout: int
) -> List[str]:
    """
    Find meaningful connections between a word and other words in the list.
    
    Args:
        word: The word to find connections for
        all_words: List of all available words
        num_connections: Number of connections to find
        model: AI model to use
        temperature: Controls randomness in generation
        timeout: API request timeout in seconds
    
    Returns:
        List of connected words
    """
    prompt = load_prompt(FIND_CONNECTIONS_PROMPT)
    full_prompt = f"{prompt}\n\nWord: {word}\nAvailable words: {', '.join(all_words)}\nNumber of connections: {num_connections}"
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": full_prompt}],
        temperature=temperature,
        timeout=timeout
    )
    raw_content = response.choices[0].message.content
    # Debug: print the raw response for the first word only
    if word == all_words[0]:
        print("\n--- RAW OPENAI RESPONSE ---")
        print(raw_content)
        print("--- END RAW RESPONSE ---\n")
    try:
        result = json.loads(raw_content)
        if isinstance(result, list):
            connections = result
        elif isinstance(result, dict) and 'connections' in result and isinstance(result['connections'], list):
            connections = result['connections']
        else:
            raise ValueError("Response is not a list or a dict with 'connections' list")
        # Filter: remove self and any word not in all_words
        filtered = [w for w in connections if w != word and w in all_words]
        return filtered[:num_connections]
    except (json.JSONDecodeError, ValueError) as e:
        print(f"Error parsing connections for {word}: {e}")
        print(f"Raw response was: {raw_content}")
        return []

def generate_description(
    word: str,
    connections: List[str],
    model: str,
    temperature: float,
    timeout: int
) -> str:
    """
    Generate a wiki-style description for a word incorporating its connections.
    
    Args:
        word: The word to describe
        connections: List of connected words
        model: AI model to use
        temperature: Controls randomness in generation
        timeout: API request timeout in seconds
    
    Returns:
        Generated description
    """
    prompt = load_prompt(GENERATE_DESCRIPTION_PROMPT)
    
    # Prepare the prompt with the word and its connections
    full_prompt = f"{prompt}\n\nWord: {word}\nConnections: {', '.join(connections)}"
    
    # Make the API call
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": full_prompt}],
        temperature=temperature,
        timeout=timeout
    )
    
    return response.choices[0].message.content.strip()

# ============================================================================
# GENERATION PROCESS
# ============================================================================

def generate_connections(words: list) -> dict:
    """
    Generate connections between words in the list.
    Args:
        words: List of word strings to find connections for
    Returns:
        Dictionary mapping words to their connections
    """
    word_graph = {}
    if os.path.exists(OUTPUT_GRAPH_FILE):
        word_graph = {item['word']: item for item in json.load(open(OUTPUT_GRAPH_FILE, 'r'))}
    for word in words:
        if word in word_graph and 'connections' in word_graph[word]:
            print(f"Skipping {word} - connections already exist")
            continue
        print(f"Finding connections for: {word}")
        if word not in word_graph:
            word_graph[word] = {}
        connections = find_connections(
            word=word,
            all_words=words,
            num_connections=NUM_CONNECTIONS,
            model=MODEL_FOR_LINKS,
            temperature=AI_TEMPERATURE,
            timeout=AI_REQUEST_TIMEOUT
        )
        word_graph[word]['connections'] = connections
        save_word_graph(word_graph, OUTPUT_GRAPH_FILE)
        time.sleep(SECONDS_BETWEEN_API_CALLS)
    return word_graph

def generate_descriptions(word_graph: Dict[str, Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
    """
    Generate descriptions for words based on their connections.
    
    Args:
        word_graph: Dictionary containing words and their connections
    
    Returns:
        Updated word graph with descriptions
    """
    # Process each word
    for word, data in word_graph.items():
        # Skip if word already has a description
        if 'description' in data:
            print(f"Skipping {word} - description already exists")
            continue
        
        # Skip if word doesn't have connections
        if 'connections' not in data:
            print(f"Skipping {word} - no connections found")
            continue
        
        print(f"Generating description for: {word}")
        
        # Generate description
        description = generate_description(
            word=word,
            connections=data['connections'],
            model=MODEL_FOR_DESCRIPTIONS,
            temperature=AI_TEMPERATURE,
            timeout=AI_REQUEST_TIMEOUT
        )
        
        # Update graph
        word_graph[word]['description'] = description
        
        # Save progress after each word
        save_word_graph(word_graph, OUTPUT_GRAPH_FILE)
        
        # Rate limiting
        time.sleep(SECONDS_BETWEEN_API_CALLS)
    
    return word_graph

def main():
    with open(WORDS_FILE, 'r') as f:
        words = json.load(f)
    print(f"Loaded {len(words)} words from {WORDS_FILE}")
    print("\nGenerating connections...")
    word_graph = generate_connections(words)
    print("\nGenerating descriptions...")
    word_graph = generate_descriptions(word_graph)
    print(f"\nGeneration complete! Word graph saved to {OUTPUT_GRAPH_FILE}")

if __name__ == "__main__":
    main() 