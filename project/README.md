# Medical Disease Diagnosis program

This project is a Medical Diagnosis of diseases implemented in Python. This program allows users to input their symptoms and matches their symptoms to potential diseases from a dataset.
The system also includes an autocomplete feature to help users input symptoms quickly and accurately.

## Video URL
https://www.youtube.com/watch?v=eddzyXA0g-s

## Features

- Input patient name, age, and symptoms.
- Match entered symptoms to potential diseases using fuzzy matching.
- Autocomplete feature for symptom input.
- Display matched diseases based on entered symptoms.
- Option to add another diagnosis or exit the program.
- Delete patient data after the session.
- minimum three symptoms user have to enter for output otherwise program will reprompt the user
- if the symptoms do not match any disease the programme will reprompt for more symptoms

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
    pip install fuzzywuzzy
    pip install python-Levenshtein 
    pip install tabulate 
    pip inatall pytest
```
2. Clone the repository:
```bash
    git clone https://github.com/imsidharthj/cs50.git
    cd project
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
Reads a CSV file and converts each row into a dictionary entry where each disease is a key and its symptoms are stored as a list of values. If the primary dataset is not found programme will use a dafult database that is hard coded in project.py

### `auto_completer(text, state)`
Provides autocomplete suggestions for symptom input based on the entered text. when user type similar letters of symptom name programme and than press tab auto completer will complete the symptom name, if user press tab more than one time it can suggest multiple similar symptoms at once

### `match_symptoms(diseases_dict, symptoms_to_match, threshold=80)`
Matches the entered symptoms to potential diseases using fuzzy matching. It matches the string on the level of 0-100 if user don't give symptom name exactly same as dataset it will match the string on similarity level and proced t output

### `handle_patient_data(diseases_dict)`
Handles the patient data input, symptom matching, and display of matched diseases. It provides a more readable user interface, check for minimum three symptoms for optimum accuracy of disease name, than arrange the data in table format after the match

### `load_default_disease_data()`
Loads a predefined dictionary of diseases and their symptoms. If `dataset.csv` not found

## Testing

The project includes tests for key functionalities using `pytest`. The test file `test_project.py` covers loading disease data, the autocomplete feature, and symptom matching.

To run the tests:
```
pytest test_project.py
```