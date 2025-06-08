import json
import os
import random

def get_existing_tag_combinations(directory):
    """Reads all batch files and returns a set of existing tag combinations."""
    existing_combinations = set()
    if not os.path.exists(directory):
        return existing_combinations

    for filename in sorted(os.listdir(directory)):
        if filename.startswith('batch_') and filename.endswith('.json'):
            filepath = os.path.join(directory, filename)
            try:
                with open(filepath, 'r') as f:
                    data = json.load(f)
                    for item in data:
                        # Create a frozenset of the tags dictionary items to make it hashable
                        if 'tags' in item and isinstance(item['tags'], dict):
                            tags_tuple = tuple(sorted(item['tags'].items()))
                            existing_combinations.add(tags_tuple)
            except (json.JSONDecodeError, IOError) as e:
                print(f"Warning: Could not read or parse {filename}: {e}")
    return existing_combinations

def get_next_batch_number(directory):
    """Determines the next batch number by checking existing files."""
    if not os.path.exists(directory):
        return 1
    
    batch_numbers = [
        int(f.replace('batch_', '').replace('.json', ''))
        for f in os.listdir(directory)
        if f.startswith('batch_') and f.endswith('.json') and f.replace('batch_', '').replace('.json', '').isdigit()
    ]
    return max(batch_numbers) + 1 if batch_numbers else 1


def main():
    """Generates a new batch of unique word prompts."""
    # --- Configuration ---
    TAG_CATEGORIES = {
        "Domain": ["tech", "science", "history", "fiction", "philosophy", "art", "nature", "emotion", "pop culture", "economics & work", "education & learning", "spirituality", "health & wellness"],
        "Culture": ["African", "East Asian", "South Asian", "Central Asian", "Middle Eastern", "Western", "Latinx", "Caribbean", "Pacific Islander", "Global Indigenous", "Diasporic", "Hybrid / global culture"],
        "Generation": ["Ancient / Classical", "Boomer", "Gen X", "Millennial", "Gen Z", "Gen Alpha", "Futuristic", "Timeless"],
        "IdentityExperience": ["immigrant / refugee", "diaspora", "racialized / minority", "working-class / underpaid", "LGBTQ+", "gender-expansive / trans", "disabled / chronically ill", "mental health experience", "neurodivergent", "spiritual seeker"],
        "PersonalityLens": ["thinker", "feeler", "doer", "dreamer", "analyst", "organizer", "rebel", "healer", "explorer", "mystic"],
        "Setting": ["city", "jungle", "outer space", "internet", "school", "home", "factory", "street", "village", "underground", "market", "temple", "dorm room", "war zone"],
        "Subculture": ["digital/online culture", "gaming", "anime", "fandoms", "memes", "music", "fashion", "art", "nightlife", "food culture", "sports & fitness"],
        "AffectiveTone": ["joyful", "melancholic", "chaotic", "peaceful", "rebellious", "nostalgic", "mysterious", "absurd", "typically humorous"]
    }
    NUM_WORDS_TO_GENERATE = 50
    BATCH_DIR = 'candidate_batches'
    # --- End Configuration ---

    os.makedirs(BATCH_DIR, exist_ok=True)

    existing_combinations = get_existing_tag_combinations(BATCH_DIR)
    next_batch_num = get_next_batch_number(BATCH_DIR)
    
    print(f"Found {len(existing_combinations)} existing tag combinations.")
    print(f"Generating new file: batch_{next_batch_num}.json")

    new_words = []
    
    while len(new_words) < NUM_WORDS_TO_GENERATE:
        num_tags = random.randint(3, 4)
        chosen_categories = random.sample(list(TAG_CATEGORIES.keys()), num_tags)
        
        tags = {}
        for category in chosen_categories:
            tags[category] = random.choice(TAG_CATEGORIES[category])
        
        tags_tuple = tuple(sorted(tags.items()))
        
        if tags_tuple not in existing_combinations:
            existing_combinations.add(tags_tuple)
            word_entry = {
                "word": "",
                "tags": tags
            }
            new_words.append(word_entry)

    output_filename = os.path.join(BATCH_DIR, f'batch_{next_batch_num}.json')
    with open(output_filename, 'w') as f:
        json.dump(new_words, f, indent=2)

    print(f"Successfully generated {len(new_words)} new prompts in {output_filename}.")


if __name__ == "__main__":
    main() 