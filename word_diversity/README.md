# Word Diversity System

This directory contains tools and definitions for analyzing and managing the diversity of the word set. It helps ensure the game's word list represents a wide range of concepts, cultures, and perspectives.

## Components

### `tags.py`
Defines the tag dimensions used to categorize words for diversity analysis:
- Generation (e.g., Gen Z, Millennial, Boomer)
- Culture (e.g., Western, African, East Asian)
- Domain (e.g., tech, art, philosophy)
- Identity Experience (e.g., disabled, immigrant, working-class)
- And more...

These tags help track and analyze the distribution of different types of words in the game.

### Word List Structure
The diversity-tagged word list (`word_lists/words_with_diversity_tags.json`) uses these tags to categorize each word:
```json
{
  "word": "example",
  "tags": {
    "Generation": "Gen Z",
    "Culture": "Western",
    "Domain": "tech",
    "IdentityExperience": "immigrant",
    ...
  }
}
```

## Usage

### Analyzing Word Diversity
1. Use the tags to analyze the distribution of words across different dimensions
2. Identify gaps or over-representation in certain categories
3. Make informed decisions about adding new words to improve diversity

### Adding New Words
When adding new words to `words_with_diversity_tags.json`:
1. Consider which tags apply to the word
2. Ensure balanced representation across different dimensions
3. Run the word list generator to update the game's word list

## Best Practices

1. **Balance**: Aim for a balanced distribution across tag dimensions
2. **Representation**: Ensure diverse perspectives and experiences are represented
3. **Inclusivity**: Consider how different players might relate to the words
4. **Relevance**: Choose words that are meaningful and relevant to their categories

## Note
The diversity tags are used for analysis and ensuring a diverse word set, but they don't affect the actual gameplay. The game uses the simplified word list (`word_lists/words.json`) for finding connections and generating descriptions. 