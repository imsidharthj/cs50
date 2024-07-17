import pytest
from io import StringIO
import os
from project import load_disease_data, load_default_disease_data, auto_completer, match_symptoms, unique_symptoms

@pytest.fixture
def csv_data():
    return StringIO("disease,symptom1,symptom2,symptom3\nFlu,fever,cough,sore throat\nCold,sneezing,runny nose,headache")

@pytest.fixture
def diseases_dict():
    return {
        'Flu': ['fever', 'cough', 'sore throat'],
        'Cold': ['sneezing', 'runny nose', 'headache']
    }

@pytest.fixture
def unique_symptoms_set():
    return {'fever', 'cough', 'sore throat', 'sneezing', 'runny nose', 'headache'}

def test_load_disease_data(csv_data, diseases_dict):
    with open('test_dataset.csv', 'w') as f:
        f.write("disease,symptom1,symptom2,symptom3\nFlu,fever,cough,sore throat\nCold,sneezing,runny nose,headache")
    result = load_disease_data('test_dataset.csv')
    assert result == diseases_dict
    os.remove('test_dataset.csv')

def test_load_default_disease_data():
    result = load_default_disease_data()
    expected_dict = {
        "Chronic cholestasis": ["itching", "vomiting", "yellowish_skin", "nausea", "loss_of_appetite", "abdominal_pain", "yellowing_of_eyes"]
    }
    assert result == expected_dict
    assert unique_symptoms.issuperset(set(expected_dict["Chronic cholestasis"]))

def test_auto_completer(unique_symptoms_set):
    # Add some symptoms to the unique_symptoms set
    unique_symptoms.update(unique_symptoms_set)
    input_text = "fe"
    expected_output = 'fever'
    result = auto_completer(input_text, 0)
    assert result == expected_output

def test_match_symptoms(diseases_dict):
    symptoms_to_match = ['fever', 'cough']
    expected_output = ['Flu']
    result = match_symptoms(diseases_dict, symptoms_to_match)
    assert result == expected_output
