print("Patient Registration Module")
patient_records = []

def register_patient(name, age):
    patient_records.append({"name": name, "age": age})
    print(f"Registered {name}, Age: {age}")

register_patient("Alice", 30)
