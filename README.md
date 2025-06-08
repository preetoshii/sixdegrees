# Six Degrees Word Graph Generator

This project contains a set of scripts to build a connected graph of words for the "Six Degrees" game. It reads a collection of words from JSON batch files, uses an AI to determine the most relevant connections between them, and then generates a wiki-style description for each word that incorporates those connections.

The system is designed to be **iterable**, allowing you to easily update your word lists and regenerate the entire game's knowledge graph with a single command.

## Project Structure

- `generate_word_graph.py`: The main script that orchestrates the entire process.
- `config.py`: A centralized configuration file for all settings (file paths, AI models, etc.).
- `ai_client.py`: Handles all communication with the OpenAI API.
- `utils.py`: Contains helper functions for loading data and saving files.
- `tags.py`: Defines the canonical tag structure for the game's words.
- `candidate_batches/`: The directory where you should store your word lists in JSON format.
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

## How to Run

To generate or update the `word_graph.json` file, simply run the main script:

```bash
python3 generate_word_graph.py
```

The script will:
- Load all words from the `candidate_batches/` directory.
- Check for an existing `word_graph.json` to resume progress.
- Go through each word to find its 3-5 closest connections using the AI.
- Go through each word again to generate a descriptive paragraph using the AI.
- Save the final, complete graph to `word_graph.json`.

The script is designed to be **resumable**. If it's interrupted, you can simply run it again, and it will pick up where it left off.

## How to Iterate on Your Game

This workflow makes iteration simple and safe:

1.  **Modify Your Words:** Add, delete, or change any of the JSON files in the `candidate_batches/` directory.
2.  **(Optional) Modify the AI's Instructions:** Edit the text files in the `prompts/` directory to change how the AI finds connections or writes descriptions.
3.  **Regenerate the Graph:** Run `python3 generate_word_graph.py`.
4.  **Done:** The `word_graph.json` file is now completely up-to-date with your latest changes. 