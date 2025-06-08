# --- utils.py ---

import os
import json

def load_all_words(directory):
    """
    Loads all word entries from JSON files in the specified directory.
    Returns a dictionary of words, where the key is the word name.
    """
    all_words = {}
    print(f"Loading words from '{directory}'...")
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            filepath = os.path.join(directory, filename)
            try:
                with open(filepath, 'r') as f:
                    data = json.load(f)
                    for item in data:
                        # The word itself is the primary key
                        word = item.get('word')
                        if word:
                            all_words[word] = item
            except (json.JSONDecodeError, TypeError) as e:
                print(f"Warning: Could not read or parse {filename}. Error: {e}")
    print(f"Successfully loaded {len(all_words)} unique words.")
    return all_words

def save_word_graph(word_graph, output_file):
    """
    Saves the final word graph dictionary to a JSON file.
    The output is a list of word objects.
    """
    print(f"Saving word graph to '{output_file}'...")
    # Convert the dictionary graph into a list for the final JSON
    output_list = list(word_graph.values())
    
    with open(output_file, 'w') as f:
        json.dump(output_list, f, indent=2)
    print("Save complete.") 