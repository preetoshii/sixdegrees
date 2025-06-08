import json
import random

# 1. Dimensions & Options for Tagging Each Word
TAG_DIMENSIONS = {
    "Domain": [
        "tech", "nature", "emotion", "fiction", "philosophy", "history",
        "spirituality", "science", "pop culture", "education & learning",
        "economics & work", "health & wellness"
    ],
    "Culture": [
        "Western", "South Asian", "East Asian", "African", "Latinx",
        "Middle Eastern", "Central Asian", "Caribbean", "Pacific Islander",
        "Global Indigenous", "Diasporic", "Hybrid / global culture"
    ],
    "Generation": [
        "Boomer", "Gen X", "Millennial", "Gen Z", "Gen Alpha",
        "Ancient / Classical", "Futuristic", "Timeless"
    ],
    "PersonalityLens": [
        "thinker", "feeler", "doer", "dreamer", "organizer", "rebel",
        "healer", "mystic", "explorer", "analyst"
    ],
    "IdentityExperience": [
        "LGBTQ+", "neurodivergent", "disabled / chronically ill",
        "mental health experience", "gender-expansive / trans",
        "racialized / minority", "immigrant / refugee",
        "working-class / underpaid", "spiritual seeker", "diaspora"
    ],
    "Subculture": [
        "gaming", "music", "memes", "art", "anime", "fashion",
        "food culture", "sports & fitness", "nightlife",
        "digital/online culture", "fandoms"
    ],
    "Setting": [
        "home", "school", "street", "market", "internet", "jungle",
        "war zone", "temple", "factory", "city", "village", "dorm room",
        "underground", "outer space"
    ],
    "AffectiveTone": [
        "joyful", "melancholic", "typically humorous", "chaotic",
        "nostalgic", "mysterious", "peaceful", "rebellious", "absurd"
    ]
}

def generate_tag_combinations(num_combinations, num_tags_per_combination_range=(3, 4)):
    """
    Generates a list of diverse tag combinations to be used as prompts for word generation.
    """
    combinations = []
    seen_combinations = set()
    dimension_names = list(TAG_DIMENSIONS.keys())

    while len(combinations) < num_combinations:
        num_tags = random.randint(*num_tags_per_combination_range)
        chosen_dimensions = random.sample(dimension_names, num_tags)
        
        combo = {}
        for dim in sorted(chosen_dimensions): # Sort for consistent key order
            combo[dim] = random.choice(TAG_DIMENSIONS[dim])
        
        # Use a frozenset of items to check for uniqueness, as dicts are not hashable
        combo_tuple = tuple(sorted(combo.items()))
        if combo_tuple not in seen_combinations:
            seen_combinations.add(combo_tuple)
            combinations.append(combo)
    
    return combinations

def load_existing_words(filename):
    """Loads existing words from a JSON file."""
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_words(filename, words):
    """Saves a list of words to a JSON file."""
    with open(filename, 'w') as f:
        json.dump(words, f, indent=2)

def get_existing_tag_tuples(words):
    """Extracts a set of existing tag combinations from a list of words."""
    existing_tuples = set()
    for item in words:
        # Ensure 'tags' key exists and is a dictionary
        if 'tags' in item and isinstance(item['tags'], dict):
            combo_tuple = tuple(sorted(item['tags'].items()))
            existing_tuples.add(combo_tuple)
    return existing_tuples

def main():
    """
    Main function to generate candidate words and save them to a file.
    """
    output_filename = 'candidate_words.json'
    
    # Load existing words and their tag combinations
    existing_words = load_existing_words(output_filename)
    existing_combinations = get_existing_tag_tuples(existing_words)
    
    print(f"Loaded {len(existing_words)} existing words from '{output_filename}'.")

    # PHASE 1: Generate a candidate list of words
    print("PHASE 1: Generating new candidate words...")
    
    # Ask user how many new words to generate
    while True:
        try:
            num_new_words_str = input("How many new words would you like to generate in this batch? ")
            num_new_words = int(num_new_words_str)
            if num_new_words > 0:
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Step 1: Build a Grid of Tag Combinations
    print(f"Generating {num_new_words} unique tag combinations...")
    
    # Generate new, unique combinations
    new_prompts = []
    seen_combinations = existing_combinations.copy()
    
    while len(new_prompts) < num_new_words:
        # Generate one combination at a time to check for uniqueness against the large existing set
        combo = generate_tag_combinations(1)[0]
        combo_tuple = tuple(sorted(combo.items()))
        if combo_tuple not in seen_combinations:
            seen_combinations.add(combo_tuple)
            new_prompts.append(combo)

    # In a real interactive process, I (the AI) would now generate the words.
    # For this script, we'll create placeholder entries to be filled in later.
    new_word_entries = []
    for prompt in new_prompts:
        new_word_entries.append({
            "word": "", # To be filled in by the AI
            "tags": prompt
        })

    # For demonstration, we'll save the combined list with placeholders.
    # The next step in the workflow would be for me to populate these.
    all_words = existing_words + new_word_entries
    save_words(output_filename, all_words)

    print(f"\nSuccessfully added {len(new_word_entries)} new word prompts.")
    print(f"Total words in '{output_filename}': {len(all_words)}.")
    print("Next step: I will now generate a word for each of the new prompts.")

if __name__ == '__main__':
    main() 