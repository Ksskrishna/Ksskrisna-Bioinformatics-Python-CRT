class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def Get_details(self):
        print(f"\nPerson's details:")
        print(f"Person's name: {self.name}")
        print(f"Person's age: {self.age}")
        print(f"Person's gender: {self.gender}")

class Patient(Person):
    def __init__(self,name,age,gender,disease):
        super()._init_(name,age,gender)
        self.disease=disease
    def Get_details(self):
        print(f"\nPatient's details:")
        print(f"Patient's name: {self.name}")
        print(f"Patient's age: {self.age}")
        print(f"Patient's gender: {self.gender}")
        print(f"Patient's Disease: {self.disease}")

class Doctor(Person):
    def _init_(self,name,age,gender,speciality):
        super()._init_(name,age,gender)
        self.speciality=speciality
        self.__patients=[]
    def Assignpatient(self,patient):
        self.__patients.append(patient)
    def get_doctor_details(self):
        return f"{self.get_details()}, Specialization: {self.speciality}"
    def get_assigned_patients(self):
        if not self.__patients:
            return "No patients assigned."
        result=""
        for p in self.__patients:
            result+=f"- {p.name} ({p.disease})\n"
        return result.strip()
doctors=[]
patients=[]

def find_doctor_by_name(name):
    for doc in doctors:
        if doc.name.lower()==name.lower():
            return doc
    return None

def find_patient_by_name(name):
    for pat in patients:
        if pat.name.lower==name.lower():
            return pat
    return None

def main():
    while True:
        print("\n--- Hospital Management System ---")
        print("1. Register Doctor")
        print("2. Register Patient")
        print("3. Assign Patient to Doctor")
        print("4. View Doctor and Assigned Patients")
        print("5. View Patient Details")
        print("6. Exit")
        choice=input("Enter your choice(1-6):")
        if choice=='1':
            name=input("Doctor Name: ")
            age=int(input("Doctor's Age: "))
            gender=input("Doctor's Gender: ")
            speciality=input("Specialization: ")
            doc=Doctor(name,age,gender,speciality)
            doctors.append(doc)
            print("Doctor registered successfully.")
        elif choice=='2':
            name=input("Patient Name: ")
            age=int(input("Patient's Age: "))
            gender=input("Patient's Gender: ")
            disease=input("Disease: ")
            doc=Doctor(name,age,gender,disease)
            patients.append(pat)
            print("Patient registered successfully.")
        elif choice=='3':
            patient_name=input("Enter Patient Name: ")
            doctor_name=input("Enter Doctor Name: ")
            pat=find_patient_by_name(patient_name)
            doc=find_doctor_by_name(doctor_name)
            if pat and doc:
                doc.assign_patient(pat)
                print("Patient assigned successfully.")
            else:
                print("Doctor or Patient not fornd.")
        elif choice=='4':
            doctor_name=input("Enter Doctor Name: ")
            doc=find_doctor_by_name(doctor_name)
            if doc:
                print(doc.get_doctor_details())
                print("Assigned Patients: ")
                print(doc.get_assigned_patients())
            else:
                print("Doctor not found.")
        elif choice=='5':
            patient_name=input("Enter Patient Name: ")
            pat=find_patient_by_name(patient_name)
            if pat:
                print(pat.get_patient_details())
            else:
                print("Patient not found.")
        elif choice=='6':
            print("Exiting the System")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
if __name__=='__main__':
    main()