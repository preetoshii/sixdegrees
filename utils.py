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
    The output is a list of word objects, each with a 'word' key and a 'connections' key (and 'description' if present).
    """
    print(f"Saving word graph to '{output_file}'...")
    output_list = []
    for word, data in word_graph.items():
        entry = {"word": word}
        if "connections" in data:
            entry["connections"] = data["connections"]
        if "description" in data:
            entry["description"] = data["description"]
        output_list.append(entry)
    with open(output_file, 'w') as f:
        json.dump(output_list, f, indent=2)
    print("Save complete.")

def generate_simple_word_list(tagged_words_file: str, output_file: str) -> None:
    """
    Generate a simple word list from a diversity-tagged word list.
    This function extracts just the words from the tagged list, removing all tag data
    to create a clean list of words for the game.
    
    Args:
        tagged_words_file: Path to the JSON file containing words with diversity tags
        output_file: Path where the simple word list will be saved
    """
    # Load the tagged words
    with open(tagged_words_file, 'r') as f:
        tagged_words = json.load(f)
    # Extract just the words as a list of strings
    words = [item['word'] for item in tagged_words if item.get('word')]
    # Save the simplified list
    with open(output_file, 'w') as f:
        json.dump(words, f, indent=2)
    print(f"Generated simple word list with {len(words)} words at {output_file}") 