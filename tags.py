# --- tags.py ---

"""
This file contains the canonical definition of the tag system for the game.
It defines the dimensions and the possible options for each dimension,
serving as a source of truth for the game's design.
"""

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