import json
import os
from collections import defaultdict

# Define word replacements and removals
WORD_REPLACEMENTS = {
    "acting-my-age": "maturity",
    "affective-labor": "empathy",
    "art-collective": "collective",
    "art-history": "aesthetics",
    "artist-in-residence": "residency",
    "comfort-character": "comfort",
    "comfort-food": "comfort",
    "company-store": "company",
    "company-town": "company",
    "corporate-meme": "meme",
    "cosmic-horror": "cosmic",
    "emotional-labor": "empathy",
    "faith-healing": "healing",
    "flea-market": "market",
    "flow-state": "flow",
    "food-desert": "desert",
    "food-porn": "food",
    "foreign-exchange": "exchange",
    "gender-affirming-care": "affirmation",
    "generation-ship": "generation",
    "generative-art": "generative",
    "guerilla-art": "guerilla",
    "health-goth": "goth",
    "heirloom-recipe": "heirloom",
    "industrial-music": "industrial",
    "installation-art": "installation",
    "lo-fi-hip-hop": "lo-fi",
    "mad-scientist": "scientist",
    "manifest-destiny": "manifest",
    "school-uniform": "uniform",
    "seed-bomb": "seed",
    "self-care": "care",
    "self-dx": "diagnosis",
    "self-medicate": "medicate",
    "space-communism": "space",
    "space-cowboy": "cowboy",
    "space-elevator": "elevator",
    "space-oddity": "oddity",
    "space-tourism": "tourism",
    "special-education": "education",
    "speculative-fiction": "speculative",
    "stan-culture": "stan",
    "afro-beats": "afrobeats",
    "afro-futurism": "afrofuturism",
    "afro-psychology": "psychology",
    "head-canon": "headcanon",
    "mana-regen": "mana"
}

# Only removing a few words that are truly redundant or problematic
WORDS_TO_REMOVE = {
    "lynching",  # Too sensitive/historical
    "gulag",     # Too historical/political
    "intifada"   # Too political
}

# Words that should keep their hyphens (established compound words or specific terms)
KEEP_HYPHENS = {
    "afro-beats", "afro-futurism", "afro-psychology", "art-brut", "bio-art", "bio-hacker",
    "bio-horror", "bio-luminary", "bio-luminescence", "bio-punk", "clown-core", "co-op",
    "crip-lit", "crip-time", "cyber-goth", "cyber-grief", "cyber-idol", "cyber-punk",
    "cyber-rebellion", "cyber-war", "dark-matter", "dark-web", "diy-biology", "e-boy",
    "e-girl", "folk-music", "garage-band", "glitch-art", "glow-up", "goth-rock",
    "head-canon", "jam-session", "juke-joint", "karma-yoga", "land-art", "math-rock",
    "mech-pilot", "meta-modernism", "mind-palace", "mono-no-aware", "mosh-pit",
    "mud-bath", "neuro-harmony", "neuro-punk", "oral-history", "oral-tradition",
    "ponzi-scheme", "protest-art", "punk-rock", "rage-quit", "retro-gaming",
    "ruin-porn", "sarmatian-punk", "side-hustle", "side-quest", "sound-healing",
    "space-oddity", "star-map", "stim-toy", "tie-dye", "tiki-bar", "tiki-culture",
    "torch-song", "vestal-virgin", "wabi-sabi", "zen-garden"
}

# Words that should be converted to spaces (concepts that are better represented as separate words)
CONVERT_TO_SPACES = {
    "acting my age", "after hours", "agent orange", "agri tech", "art collective",
    "art history", "artist in residence", "astral projection", "comfort character",
    "comfort food", "company store", "company town", "corporate meme", "cosmic horror",
    "emotional labor", "faith healing", "film noir", "flame war", "flash mob",
    "flea market", "flow state", "food desert", "food porn", "foreign exchange",
    "freudian slip", "gallows humor", "game show", "gamified learning", "gender fluid",
    "gender reveal", "generation ship", "generative art", "gen z humor", "gig economy",
    "glam rock", "guerilla art", "guerilla gardening", "health goth", "heirloom recipe",
    "industrial music", "installation art", "kawaii metal", "kick on", "kin keeping",
    "land back", "last supper", "late night tv", "lawrence of arabia", "liminal space",
    "lo fi hip hop", "mad scientist", "manic pixie dream girl", "manifest destiny",
    "meme lord", "meme stock", "mor style", "pyramid scheme", "quantified self",
    "queer coding", "queer rage", "queer theory", "rage room", "reality tv",
    "red scare", "reggae sunsplash", "restorative justice", "school uniform",
    "seed bomb", "self care", "self dx", "self medicate", "space communism",
    "space cowboy", "space elevator", "space opera", "space suit", "space tourism",
    "special education", "speculative fiction", "stan culture", "star trek",
    "stardew valley", "swap meet", "sweat lodge", "talk show", "talk story",
    "tang ping", "teach for america", "teddy boy", "teen angst", "teen movie",
    "terra nullius", "the blues", "the medium is the message", "third culture kid",
    "third eye", "third place", "trad goth", "trauma informed", "trench art",
    "troll farm", "tumblr era", "tv dinner", "two spirit", "ubiquitous computing",
    "zen garden meditation", "zen painting", "zoot suit"
}

def load_all_batches():
    batches = {}
    seen_words = set()
    duplicate_words = set()
    
    # Load all batch files
    for filename in os.listdir('candidate_batches'):
        if filename.endswith('.json'):
            with open(os.path.join('candidate_batches', filename), 'r') as f:
                try:
                    data = json.load(f)
                    # Track duplicates
                    for item in data:
                        word = item['word']
                        if word in seen_words:
                            duplicate_words.add(word)
                        seen_words.add(word)
                    batches[filename] = data
                except json.JSONDecodeError:
                    print(f"Error reading {filename}")
    
    return batches, duplicate_words

def clean_tags(tags):
    # Remove duplicate tags
    cleaned_tags = {}
    for key, value in tags.items():
        if key not in cleaned_tags:
            cleaned_tags[key] = value
    return cleaned_tags

def clean_batches():
    batches, duplicate_words = load_all_batches()
    
    # Create a mapping of words to their best entry
    word_entries = {}
    for filename, data in batches.items():
        for item in data:
            word = item['word']
            
            # Skip words that should be removed
            if word in WORDS_TO_REMOVE:
                continue
                
            # Replace word if it's in the replacement dictionary
            if word in WORD_REPLACEMENTS:
                word = WORD_REPLACEMENTS[word]
                item['word'] = word
            
            # Convert hyphens to spaces for words in CONVERT_TO_SPACES
            if word in CONVERT_TO_SPACES:
                word = CONVERT_TO_SPACES[word]
                item['word'] = word
            
            # If we haven't seen this word before or if this entry has more tags
            if word not in word_entries or len(item['tags']) > len(word_entries[word]['tags']):
                word_entries[word] = item
    
    # Create new batches with unique words
    new_batches = defaultdict(list)
    batch_size = 30  # Target size for each batch
    
    # Sort words to ensure consistent distribution
    sorted_words = sorted(word_entries.keys())
    
    # Distribute words across batches
    for i, word in enumerate(sorted_words):
        batch_num = (i // batch_size) + 1
        entry = word_entries[word]
        entry['tags'] = clean_tags(entry['tags'])
        new_batches[f'batch_{batch_num}.json'].append(entry)
    
    # Save cleaned batches
    for filename, data in new_batches.items():
        with open(os.path.join('candidate_batches', filename), 'w') as f:
            json.dump(data, f, indent=2)
    
    print(f"Found {len(duplicate_words)} duplicate words")
    print(f"Created {len(new_batches)} cleaned batch files")
    print(f"Removed {len(WORDS_TO_REMOVE)} words")
    print(f"Replaced {len(WORD_REPLACEMENTS)} words")
    print(f"Converted {len(CONVERT_TO_SPACES)} hyphenated words to spaces")
    print(f"Kept {len(KEEP_HYPHENS)} hyphenated words")

if __name__ == "__main__":
    clean_batches() 