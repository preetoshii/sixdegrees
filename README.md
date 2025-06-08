# Six Degrees Word Graph Generator

This project contains a set of scripts to build a connected graph of words for the "Six Degrees" game. It reads a collection of words from a JSON file, uses an AI to determine the most relevant connections between them, and then generates a wiki-style description for each word that incorporates those connections.

The system is designed to be **iterable**, allowing you to easily update your word list and regenerate the entire game's knowledge graph with a single command.

## Project Structure

- `config.py`: A centralized configuration file for all settings (file paths, AI models, etc.).
- `ai_client.py`: Handles all communication with the OpenAI API.
- `utils.py`: Contains helper functions for loading data and saving files.
- `tags.py`: Defines the tag dimensions used in the Diverse Word Generation system.
- `word_lists/`: Directory containing the word list in JSON format.
- `description generation/`: Contains everything related to generating connections and descriptions:
  - `generate.py`: The script that generates connections and descriptions
  - `find_connections_prompt.txt`: Controls how words are connected
  - `generate_description_prompt.txt`: Controls how descriptions are written
- `word_graph.json`: The final output file that your game will use.
- `requirements.txt`: A list of the required Python packages.
- `.env.example`: A template for your environment variables.

## Setup

1.  **Clone the Repository:**
    ```bash
    git clone <your-repo-url>
    cd <your-repo-name>
    ```

2.  **Set up a Virtual Environment (Recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure your API Key:**
    -   Create a new file named `.env` in the root of the project.
    -   Add your OpenAI API key to this file, like so:
        ```
        OPENAI_API_KEY="sk-..."
        ```

5.  **Review Configuration:**
    -   Open `config.py` to review the settings. You can change the AI models, number of connections, and other parameters to suit your needs.

## Game Designer Workflow

As a game designer, you have three main ways to iterate on the game:

1.  **Modify the Word List:** Edit the `word_lists/words.json` file to add, delete, or change words. This is where you curate the actual content of your game.

2.  **Adjust Description Generation:** Edit the files in the `description generation/` directory to change how the AI finds connections between words and writes their descriptions. This controls the narrative and thematic elements of your game.

3.  **Regenerate the Game Graph:** After making any changes to the word list or description generation, run:
    ```bash
    python3 description generation/generate.py
    ```
    This will update the game's knowledge graph with your latest changes.

The `word_graph.json` file is your final output - it contains all the words, their connections, and their descriptions, ready to be used in your game. 