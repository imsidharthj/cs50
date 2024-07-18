# Medical Disease Diagnosis program

This project is a Medical Diagnosis of diseases implemented in Python. This program allows users to input their symptoms and matches their symptoms to potential diseases from a dataset.
The system also includes an autocomplete feature to help users input symptoms quickly and accurately.

## Video URL


## Features

- Input patient name, age, and symptoms.
- Match entered symptoms to potential diseases using fuzzy matching.
- Autocomplete feature for symptom input.
- Display matched diseases based on entered symptoms.
- Option to add another diagnosis or exit the program.
- Delete patient data after the session.

## Requirements

- Python 3.x
- `fuzzywuzzy` library for fuzzy matching.
- `python-Levenshtein` for improved performance (optional but recommended).
- `tabulate` library for displaying tables.
- `readline` library for autocomplete functionality (built-in on Unix-like systems, may require additional setup on Windows).
- `pytest` for running tests

## Installation

1. Install the required libraries:
```bash
    pip install fuzzywuzzy python-Levenshtein tabulate pytest
```

## TODO

1. Ensure you have a CSV file named `dataset.csv` in the same directory as the script. The CSV file should have the following format:
```csv
    disease,symptom1,symptom2,symptom3,...
    Flu,fever,cough,sore throat
    Cold,sneezing,runny nose,headache
    ...
```

2. Run the main script:
```
    python3 project.py
```

3. Follow the prompts to enter patient data and symptoms(minimum 3 symptoms). The program will display matched diseases and ask if you want to add another diagnosis.

## Functions

### `read_csv_to_dict(csv_file_path)`
Reads a CSV file and converts each row into a dictionary entry where each disease is a key and its symptoms are stored as a list of values.

### `auto_completer(text, state)`
Provides autocomplete suggestions for symptom input based on the entered text.

### `match_symptoms(diseases_dict, symptoms_to_match, threshold=80)`
Matches the entered symptoms to potential diseases using fuzzy matching.

### `handle_patient_data(diseases_dict)`
Handles the patient data input, symptom matching, and display of matched diseases.

### `load_default_disease_data()`
Loads a predefined dictionary of diseases and their symptoms. If `dataset.csv` not found

## Testing

The project includes tests for key functionalities using `pytest`. The test file `test_project.py` covers loading disease data, the autocomplete feature, and symptom matching.

To run the tests:
```
pytest test_project.py
```