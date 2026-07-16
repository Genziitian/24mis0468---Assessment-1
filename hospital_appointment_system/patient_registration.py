print("Patient Registration Module")
patient_records = []

def register_patient(name):
    patient_records.append({"name": name})
    print(f"Registered {name}")

register_patient("Alice")
