# Description Generation

This directory contains everything needed to generate the connections and descriptions for the words in your game. It is the primary place where you, as a game designer, can shape the narrative and thematic feel of the game.

## Contents

- `generate.py`: This is the main script that orchestrates the entire process. It reads your word list, calls the AI to find connections, and then calls the AI again to write descriptions based on those connections.

- `find_connections_prompt.txt`: This is a prompt file that tells the AI **how to choose which words are connected**. You can edit this file to change the *logic* of the connections. For example, you could instruct the AI to prefer thematic links, historical relationships, or even contrasting ideas.

- `generate_description_prompt.txt`: This prompt tells the AI **how to write the description** for a word, given its connections. You can edit this file to change the tone, style, and length of the descriptions. This is where you can instruct the AI to, for example, write in a more encyclopedic, poetic, or humorous style.

## How to Use

1.  **Curate Your Word List:** Make sure your primary word list in `word_lists/words.json` is up to date.
2.  **(Optional) Adjust the Prompts:** Modify the `.txt` files in this directory to change the AI's behavior.
3.  **Run the Generator:** Execute the `generate.py` script from the project root:
    ```bash
    python3 "description generation/generate.py"
    ```

The script will update the main `word_graph.json` file with the newly generated content. 