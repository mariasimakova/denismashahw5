import pytest
from patient import Patient


def test_add_test():
    patient = Patient(name="Test Patient", symptoms=["fever", "cough"])
    patient.add_test("covid", True)

    assert patient.tests["covid"] is True
    
    patient.add_test("flu", False)
    
    assert patient.tests["flu"] is False

def test_has_covid_with_covid_test():
    patient = Patient(name="Test Patient", symptoms=["fever", "cough"])
    patient.add_test("covid", True)
    assert patient.has_covid() == 0.99
    
    patient.add_test("covid", False)
    assert patient.has_covid() == 0.01

def test_has_covid_without_covid_test():
    patient_all_symptoms = Patient(name="JTest Patient 1", symptoms=["fever", "cough", "anosmia"])
    assert patient_all_symptoms.has_covid() == 0.35 
    
    patient_two_symptoms = Patient(name="Test Patient 2", symptoms=["fever", "cough"])
    assert patient_two_symptoms.has_covid() == 0.25 
    
    patient_one_symptom = Patient(name="Test Patient 3", symptoms=["fever"])
    assert patient_one_symptom.has_covid() == 0.15 
    
    patient_no_symptom = Patient(name="Test Patient 4", symptoms=["headache"])
    assert patient_no_symptom.has_covid() == 0.05