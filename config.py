# --- config.py ---

import os

# -- File System --
WORD_LISTS_DIR = "word_lists"
WORDS_FILE = os.path.join(WORD_LISTS_DIR, "words.json")  # Simple word list
DIVERSITY_TAGS_FILE = os.path.join(WORD_LISTS_DIR, "words_with_diversity_tags.json")  # Words with diversity tags
OUTPUT_GRAPH_FILE = "word_graph.json"

# -- AI Generation Settings --
NUM_CONNECTIONS = 5  # Number of connections to find per word
AI_TEMPERATURE = 0.7  # Controls randomness in generation
AI_REQUEST_TIMEOUT = 30  # Timeout for API requests in seconds

# -- AI Model Selection --
# You can use models like "gpt-4o", "gpt-4-turbo", "gpt-3.5-turbo", etc.
MODEL_FOR_LINKS = "gpt-3.5-turbo"  # Efficient for finding connections between words
MODEL_FOR_DESCRIPTIONS = "gpt-4-turbo-preview"  # Better for creative description writing

# -- Rate Limiting --
# Time to wait in seconds between consecutive calls to the AI API
# to avoid hitting rate limits. Adjust based on your API plan.
SECONDS_BETWEEN_API_CALLS = 0.2  # Minimum time between API calls

# -- Prompt File Paths --
DESCRIPTION_GEN_DIR = "description generation"
FIND_CONNECTIONS_PROMPT = os.path.join(DESCRIPTION_GEN_DIR, "find_connections_prompt.txt")
GENERATE_DESCRIPTION_PROMPT = os.path.join(DESCRIPTION_GEN_DIR, "generate_description_prompt.txt") 