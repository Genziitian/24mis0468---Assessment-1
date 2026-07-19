print("Patient Registration Module")
patient_records = []

def register_patient(name, age, phone):
    patient_records.append({"name": name, "age": age, "phone": phone})
    print(f"Registered {name}, Age: {age}, Phone: {phone}")

register_patient("Alice", 30, "555-1234")

#Modifying the file 
print("modified the file for case study 2")
