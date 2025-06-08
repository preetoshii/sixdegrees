# --- config.py ---

# -- File System --
CANDIDATE_BATCHES_DIR = 'candidate_batches'
OUTPUT_GRAPH_FILE = 'word_graph.json'

# -- AI Generation Settings --
NUM_CONNECTIONS = 5  # The number of related words to find for each target word
AI_TEMPERATURE = 0.7  # Creativity level for descriptions (0.0 to 1.0)
AI_REQUEST_TIMEOUT = 30  # Seconds to wait for a response from the AI

# -- AI Model Selection --
# You can use models like "gpt-4o", "gpt-4-turbo", "gpt-3.5-turbo", etc.
MODEL_FOR_LINKS = "gpt-4o"  # Analytical task of finding connections
MODEL_FOR_DESCRIPTIONS = "gpt-4o" # Creative task of writing descriptions

# -- Rate Limiting --
# Time to wait in seconds between consecutive calls to the AI API
# to avoid hitting rate limits. Adjust based on your API plan.
SECONDS_BETWEEN_API_CALLS = 1

# -- Prompt File Paths --
PROMPT_FOR_LINKS_FILE = 'prompts/find_connections_prompt.txt'
PROMPT_FOR_DESCRIPTIONS_FILE = 'prompts/generate_description_prompt.txt' 