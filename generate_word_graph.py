# --- generate_word_graph.py ---

import time
import os
import json
import config
import utils
import ai_client

def main():
    """
    Main function to generate the word graph.
    Orchestrates the two-step process:
    1. Generate connections for each word.
    2. Generate a wiki-style description for each word using its connections.
    """
    print("Starting word graph generation...")
    
    # Load all words from the batch files
    all_words_data = utils.load_all_words(config.CANDIDATE_BATCHES_DIR)
    all_word_names = list(all_words_data.keys())
    
    # Check if a partial graph file already exists
    if os.path.exists(config.OUTPUT_GRAPH_FILE):
        print("Existing graph file found. Loading it to resume.")
        with open(config.OUTPUT_GRAPH_FILE, 'r') as f:
            existing_data = json.load(f)
        # Convert list back to a dictionary for processing
        word_graph = {item['word']: item for item in existing_data}
    else:
        word_graph = all_words_data.copy()

    # --- Step 1: Generate Connections ---
    print("\n--- Step 1: Generating word connections ---")
    for i, target_word in enumerate(all_word_names):
        print(f"({i+1}/{len(all_word_names)}) Processing connections for '{target_word}'...")
        
        # Check if connections are already generated and valid
        if word_graph.get(target_word, {}).get('connections'):
            print("... Connections already exist. Skipping.")
            continue

        candidate_words = [w for w in all_word_names if w != target_word]
        connections = ai_client.find_connections(target_word, candidate_words)
        
        word_graph[target_word]['connections'] = connections
        
        # Save progress after each word
        utils.save_word_graph(word_graph, config.OUTPUT_GRAPH_FILE)
        time.sleep(config.SECONDS_BETWEEN_API_CALLS) 

    # --- Step 2: Generate Descriptions ---
    print("\n--- Step 2: Generating word descriptions ---")
    for i, target_word in enumerate(all_word_names):
        data = word_graph[target_word]
        print(f"({i+1}/{len(all_word_names)}) Processing description for '{target_word}'...")

        if data.get('description'):
             print("... Description already exists. Skipping.")
             continue

        required_connections = data.get('connections', [])
        if not required_connections:
            print("... No connections found. Skipping description generation.")
            continue

        description = ai_client.generate_description(target_word, required_connections)
        word_graph[target_word]['description'] = description

        # Save progress after each word
        utils.save_word_graph(word_graph, config.OUTPUT_GRAPH_FILE)
        time.sleep(config.SECONDS_BETWEEN_API_CALLS)

    print(f"\nProcess complete. Final word graph saved to '{config.OUTPUT_GRAPH_FILE}'.")

if __name__ == "__main__":
    main() 