import json
from collections import defaultdict
from tags import TAG_DIMENSIONS

# Path to the JSON file containing the tagged word list
TAGGED_WORDS_FILE = "word_lists/words.json"

def load_tagged_words(file_path: str):
    """Load words from a JSON file."""
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: The file '{file_path}' is not a valid JSON file.")
        return []

def analyze_diversity(words: list):
    """Analyzes and prints the diversity distribution of the word set."""
    if not words:
        print("The word list is empty. No analysis to perform.")
        return

    print(f"Analyzing {len(words)} words for diversity distribution...\n")

    # --- Overall Tag Distribution ---
    print("-" * 50)
    print("Overall Tag Distribution")
    print("-" * 50)
    
    for dimension, valid_tags in TAG_DIMENSIONS.items():
        tag_counts = defaultdict(int)
        
        # Count occurrences of each tag in the current dimension
        for word_obj in words:
            # Ensure 'tags' and the specific dimension exist
            if 'tags' in word_obj and dimension in word_obj['tags']:
                # The tag can be a single string or a list of strings
                tags_for_dimension = word_obj['tags'][dimension]
                if isinstance(tags_for_dimension, list):
                    for tag in tags_for_dimension:
                        if tag in valid_tags:
                            tag_counts[tag] += 1
                elif isinstance(tags_for_dimension, str):
                    if tags_for_dimension in valid_tags:
                        tag_counts[tags_for_dimension] += 1
        
        print(f"\nDimension: {dimension.replace('_', ' ').title()}")
        if not tag_counts:
            print("  No words found for this dimension.")
            continue
            
        # Print each tag's count and percentage
        total_in_dimension = sum(tag_counts.values())
        for tag in valid_tags:
            count = tag_counts.get(tag, 0)
            percentage = (count / len(words)) * 100 if len(words) > 0 else 0
            print(f"  - {tag}: {count} words ({percentage:.1f}%)")

def main():
    """Main function to run the analysis."""
    words = load_tagged_words(TAGGED_WORDS_FILE)
    analyze_diversity(words)

if __name__ == "__main__":
    main() 