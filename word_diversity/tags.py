"""
This file defines the tag dimensions for the diverse word generation system.
Each dimension represents a different facet of a word's context or feel.
This is not a definitive guide to the game's design, but rather a tool to help
generate a broad and interesting set of initial words.
"""

# Defines the different categories for tags and the possible values for each.
TAG_DIMENSIONS = {
    "generation": ["Gen Z", "Millennial", "Gen X", "Boomer"],
    "personality_lens": ["creator", "intellectual", "dreamer", "doer"],
    "setting": ["classroom", "internet", "nature", "nightclub", "workplace", "studio"],
    "identity_experience": ["racialized/minority", "queer", "spiritual seeker", "disability"],
    "subculture": ["fashion", "music", "art", "gaming", "science", "activism"],
    "domain": ["pop culture", "technology", "philosophy", "history", "religion", "fandoms", "nightlife"],
    "affective_tone": ["chaotic", "melancholic", "aspirational", "nostalgic", "ironic"],
    "culture": ["East Asian", "South Asian", "Western", "African", "Latin American", "diasporic"]
} 