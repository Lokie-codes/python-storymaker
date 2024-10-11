
# Storyline Generator

This Python project generates random storylines by selecting elements from predefined categories such as time periods, characters, places, and more. It outputs the generated stories to a JSON file and archives them for future reference.

## Project Structure

The project has the following structure:
```
.
├── input/                 # Contains input JSON file with story elements
│   └── story_inputs.json  # JSON file with predefined times, places, characters, actions, etc.
├── output/                # Contains the generated storylines
│   └── storylines.json    # Output JSON file with generated full stories
├── archive/               # Contains archived stories
│   └── story_archive.json # JSON file storing all past generated stories
├── performance.log        # Log file that tracks performance of the script
├── story_generator.py     # Main Python script for generating stories
└── README.md              # This README file
```

## How It Works

The script randomly selects story elements (such as times, places, characters, and conflicts) from a predefined JSON file to create complete storylines. These stories are saved in an output file and archived in a separate file for future reference.

The script also logs performance metrics (e.g., time taken for each operation) in `performance.log`.

## Features

- **Random Story Generation**: Randomly combines story elements from predefined categories.
- **Story Archiving**: Archives all generated stories.
- **Performance Logging**: Logs the time taken for various steps like loading input, generating stories, and saving them.
- **Modular Design**: Easily add or modify story elements by editing the `story_inputs.json` file.

## Setup and Installation

### Requirements

- Python 3.x
- The following standard Python libraries:
  - `os`
  - `json`
  - `random`
  - `time`
  - `logging`

### Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Lokie-codes/python-storymaker.git
   cd python-storymaker
   ```

2. **Create necessary directories**:
   The script will automatically create the required `input`, `output`, and `archive` directories when you run it.

3. **Prepare your story elements**:
   - Add or modify story elements in the `input/story_inputs.json` file. This JSON contains lists of times, places, characters, actions, motivations, conflicts, and outcomes.
   
   Example `story_inputs.json`:
   ```json
   {
      "times": ["In the year 2045", "In the medieval era"],
      "places": ["on Mars", "in a dark forest"],
      "characters": ["an astronaut", "a brave knight"],
      "actions": ["fought", "sought a mythical sword"],
      "motivations": ["to protect Earth", "to defend the kingdom"],
      "conflicts": ["against an alien invasion", "but faced a fierce dragon"],
      "outcomes": ["and saved humanity", "and emerged victorious"]
   }
   ```

4. **Run the script**:
   ```bash
   python main.py
   ```

5. **Generated output**:
   - Generated stories will be saved in `output/storylines.json`.
   - Archived stories will be saved in `archive/story_archive.json`.
   - Performance logs will be stored in `performance.log`.

## Usage

1. **Number of Stories**: When prompted, enter the number of storylines you would like to generate.
2. **Modifying Story Elements**: To change the story elements (times, characters, actions, etc.), edit the `input/story_inputs.json` file.

## Example Story Output

Here’s an example of a generated story:

```json
[
   "In the medieval era in a dark forest a brave knight sought a mythical sword to defend the kingdom but faced a fierce dragon and emerged victorious"
]
```

## Performance Monitoring

The script logs the time taken for various operations such as:

- Creating directories
- Loading input data
- Generating stories
- Archiving stories

Check the `performance.log` file for performance metrics.

## Future Improvements

- Add a web interface to allow users to generate stories online.
- Implement a feature to generate stories with specific themes or constraints.
- Add more categories like `weather`, `mood`, or `plot twists` for richer stories.

## License

This project is open-source and available under the MIT License.
