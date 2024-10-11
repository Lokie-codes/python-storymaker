import random
import json
import os
import time
import logging
from typing import List, Dict

# Define folder paths
INPUT_FOLDER = "input"
OUTPUT_FOLDER = "output"
ARCHIVE_FOLDER = "archive"

# Define file paths
INPUT_FILE_PATH = os.path.join(INPUT_FOLDER, "story_inputs.json")
OUTPUT_FILE_PATH = os.path.join(OUTPUT_FOLDER, "storylines.json")
ARCHIVE_FILE_PATH = os.path.join(ARCHIVE_FOLDER, "story_archive.json")

# Set up logging configuration
logging.basicConfig(
    filename='performance.log',  # Log file
    level=logging.INFO,          # Log level
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def create_folders():
    """Creates the necessary folders for input, output, and archive."""
    start_time = time.time()
    os.makedirs(INPUT_FOLDER, exist_ok=True)
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    os.makedirs(ARCHIVE_FOLDER, exist_ok=True)
    end_time = time.time()
    
    logging.info(f"Folders created. Time taken: {end_time - start_time:.4f} seconds")


def select_random_elements(data: Dict[str, List[str]]) -> List[str]:
    """Randomly selects an element from each category to form a story."""
    start_time = time.time()
    elements = [
        random.choice(data['times']),
        random.choice(data['places']),
        random.choice(data['characters']),
        random.choice(data['actions']),
        random.choice(data['motivations']),
        random.choice(data['conflicts']),
        random.choice(data['outcomes'])
    ]
    end_time = time.time()
    
    logging.info(f"Random elements selected. Time taken: {end_time - start_time:.4f} seconds")
    return elements


def load_story_input(file_path: str = INPUT_FILE_PATH) -> Dict[str, List[str]]:
    """Loads the story input data from a JSON file."""
    start_time = time.time()
    with open(file_path, 'r') as file:
        data = json.load(file)
    end_time = time.time()
    
    logging.info(f"Story input data loaded from {file_path}. Time taken: {end_time - start_time:.4f} seconds")
    return data


def generate_stories(input_data: Dict[str, List[str]], number_of_stories: int) -> List[List[str]]:
    """Generates the specified number of storylines by combining random elements."""
    start_time = time.time()
    stories = [select_random_elements(input_data) for _ in range(number_of_stories)]
    end_time = time.time()
    
    logging.info(f"Generated {number_of_stories} stories. Time taken: {end_time - start_time:.4f} seconds")
    return stories


def convert_to_full_story(story_elements: List[str]) -> str:
    """Converts a list of story elements into a full sentence."""
    return " ".join(story_elements)


def save_full_stories_to_json(stories: List[List[str]], output_file: str = OUTPUT_FILE_PATH) -> None:
    """Converts the story elements to full sentences and saves them to a JSON file."""
    start_time = time.time()
    full_storylines = [convert_to_full_story(story) for story in stories]
    
    with open(output_file, 'w') as file:
        json.dump(full_storylines, file, indent=4)
    
    end_time = time.time()
    
    logging.info(f"Full storylines saved to {output_file}. Time taken: {end_time - start_time:.4f} seconds")


def load_existing_stories(archive_file: str = ARCHIVE_FILE_PATH) -> List[str]:
    """Loads previously generated stories from the archive file."""
    start_time = time.time()
    try:
        with open(archive_file, 'r') as file:
            stories = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        stories = []  # Return an empty list if the file doesn't exist or is empty
    
    end_time = time.time()
    
    logging.info(f"Loaded existing stories from {archive_file}. Time taken: {end_time - start_time:.4f} seconds")
    return stories


def archive_stories(new_stories: List[List[str]], archive_file: str = ARCHIVE_FILE_PATH) -> None:
    """Appends new stories to the archive file."""
    start_time = time.time()
    
    existing_stories = load_existing_stories(archive_file)
    new_full_stories = [convert_to_full_story(story) for story in new_stories]
    
    # Combine existing and new stories
    all_stories = existing_stories + new_full_stories
    
    # Save all stories back to the archive file
    with open(archive_file, 'w') as file:
        json.dump(all_stories, file, indent=4)
    
    end_time = time.time()
    
    logging.info(f"Archived new stories to {archive_file}. Time taken: {end_time - start_time:.4f} seconds")


def get_number_of_stories() -> int:
    """Prompts the user for the number of stories to generate and validates input."""
    while True:
        try:
            number_of_stories = int(input("Enter the number of storylines you need: "))
            if number_of_stories > 0:
                return number_of_stories
            else:
                print("Number of storylines cannot be zero or less. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def main() -> None:
    """Main execution function."""
    logging.info("Program started.")
    create_folders()  # Create folders for input, output, and archive
    
    input_data = load_story_input()
    number_of_stories = get_number_of_stories()
    
    # Generate the storylines
    storylines = generate_stories(input_data, number_of_stories)
    
    # Save full storylines directly to 'storylines.json'
    save_full_stories_to_json(storylines)
    
    # Archive the new stories
    archive_stories(storylines)
    
    logging.info(f"Full storylines saved to '{OUTPUT_FILE_PATH}'.")
    logging.info(f"New stories archived in '{ARCHIVE_FILE_PATH}'.")


if __name__ == "__main__":
    main()
