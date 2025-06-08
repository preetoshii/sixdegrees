# Word Lists

This directory stores the source lists of words for the game.

## Files

- `words_with_diversity_tags.json`: This is the **master source of truth** for all words. It contains each word along with a set of tags that describe its various facets (culture, domain, tone, etc.). This file is used for diversity analysis and is the primary file you should edit when adding or curating words.

- `words.json`: This is a **generated file**. It contains the simplified list of words that the main game engine uses to build the word graph. You should **not** edit this file directly.

## Workflow

1.  To add or change words, edit the `words_with_diversity_tags.json` file.
2.  After editing, run the `generate_word_list.py` script from within this directory:
    ```bash
    python3 generate_word_list.py
    ```
3.  This will update the `words.json` file, making your changes available to the main game engine. 