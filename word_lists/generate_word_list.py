import sys
import os

# Add the parent directory to the Python path to allow importing from `utils`
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import generate_simple_word_list
from config import DIVERSITY_TAGS_FILE, WORDS_FILE

if __name__ == "__main__":
    print("Generating simple word list (as a list of strings) from diversity-tagged file...")
    generate_simple_word_list(DIVERSITY_TAGS_FILE, WORDS_FILE)
    print("\nProcess complete.")
    print(f"The simplified word list (list of strings) has been saved to '{WORDS_FILE}'.") 