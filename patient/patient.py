class Patient:
    def __init__(self, name: str, symptoms: list):
        self.name = name
        self.symptoms = symptoms
        self.tests = {}

    def add_test(self, test_name: str, result: bool):
        self.tests[test_name] = result

    def has_covid(self) -> float:
        if "covid" in self.tests:
            return 0.99 if self.tests["covid"] else 0.01
        
        probability = 0.05
        covid_symptoms = ["fever", "cough", "anosmia"]
        for symptom in covid_symptoms:
            if symptom in self.symptoms:
                probability += 0.1

        return round(probability, 4)
    
symptoms =  ["a", "b", "c", "fever", "cough", "anosmia"]

for i in range(1, len(symptoms)+1):
    name = f'Test {i+1}'
    patient_symptoms = symptoms[:i]
    patient = Patient(name=name, symptoms=patient_symptoms)

    print(f'Chance of {name} patient having covid with symptoms of {", ".join(patient_symptoms)}: {patient.has_covid()}')
