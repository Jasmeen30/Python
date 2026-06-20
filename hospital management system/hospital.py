# Custom Exception
class InvalidPatientError(Exception):
    pass


# Patient Class
class Patient:
    def __init__(self, patient_id, name, age):
        if age <= 0:
            raise InvalidPatientError("Age must be greater than 0.")

        self.patient_id = patient_id
        self.name = name
        self.age = age

    def display(self):
        print(f"Patient ID: {self.patient_id}")
        print(f"Name      : {self.name}")
        print(f"Age       : {self.age}")


# Doctor Class
class Doctor:
    def __init__(self, doctor_id, name, specialization):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization

    def display(self):
        print(f"Doctor ID      : {self.doctor_id}")
        print(f"Doctor Name    : {self.name}")
        print(f"Specialization : {self.specialization}")


# Dictionary to store patient records
patient_records = {}

# List to maintain patient IDs
patient_ids = []


# Function to add patient
def add_patient():
    try:
        pid = input("Enter Patient ID: ")
        name = input("Enter Patient Name: ")
        age = int(input("Enter Age: "))

        patient = Patient(pid, name, age)

        patient_records[pid] = patient
        patient_ids.append(pid)

        with open("hospital management system/patients.txt", "a") as file:
            file.write(f"{pid},{name},{age}\n")

        print("Patient record added successfully!")

    except ValueError:
        print("Invalid age! Please enter a number.")

    except InvalidPatientError as e:
        print("Error:", e)


# Function to schedule appointment
def schedule_appointment():
    pid = input("Enter Patient ID: ")

    if pid not in patient_records:
        print("Patient not found!")
        return

    doctor_name = input("Enter Doctor Name: ")
    date = input("Enter Appointment Date (DD/MM/YYYY): ")

    with open("hospital management system/appointments.txt", "a") as file:
        file.write(f"{pid},{doctor_name},{date}\n")

    print("Appointment scheduled successfully!")


# Function to display patients
def display_patients():
    if not patient_records:
        print("No patient records found.")
        return

    print("\nPatient Records")
    print("-" * 30)

    for patient in patient_records.values():
        patient.display()
        print("-" * 30)


# Main Menu
while True:
    print("\n===== Hospital Management System =====")
    print("1. Add Patient")
    print("2. Schedule Appointment")
    print("3. Display Patients")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_patient()

    elif choice == "2":
        schedule_appointment()

    elif choice == "3":
        display_patients()

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice! Try again.")