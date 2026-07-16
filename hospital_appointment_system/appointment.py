print("Hospital Appointment Booking System")

appointments = []

while True:
    print("\n1. Book Appointment")
    print("2. View Appointments")
    print("3. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        patient_name = input("Enter patient name: ")
        doctor_name = input("Enter doctor name: ")
        time = input("Enter appointment time: ")
        
        appointments.append({
            "patient": patient_name,
            "doctor": doctor_name,
            "time": time
        })
        print("Appointment successfully booked!")
        
    elif choice == '2':
        if len(appointments) == 0:
            print("No appointments booked yet.")
        else:
            print("\nCurrent Appointments:")
            for appt in appointments:
                print(appt["patient"], "-", appt["doctor"], "-", appt["time"])
                
    elif choice == '3':
        print("Exiting...")
        break
        
    else:
        print("Invalid choice. Please try again.")
