from datetime import datetime
import csv

class Patient:
    def __init__(self, patient_id, gender, race, age, ethnicity, insurance, zip_code):
        self.patient_id = patient_id
        self.gender = gender
        self.race = race
        self.age = age
        self.ethnicity = ethnicity
        self.insurance = insurance
        self.zip_code = zip_code
        self.visits = []
        self.notes = []

    def add_visit(self, visit):
        self.visits.append(visit)
        
    def add_note(self, note_id, note_type):
        self.notes.append({'note_id': note_id, 'note_type': note_type})

class Visit:
    def __init__(self, visit_id, visit_time, department, chief_complaint):
        self.visit_id = visit_id
        self.visit_time = visit_time
        self.department = department
        self.chief_complaint = chief_complaint

class Department:
    def __init__(self, name):
        self.name = name
        self.patients = []

    def add_patient(self, patient):
        self.patients.append(patient)

class Hospital:
    def __init__(self):
        self.departments = {}

    def add_department(self, department_name):
        if department_name not in self.departments:
            self.departments[department_name] = Department(department_name)

    def add_patient_to_department(self, department_name, patient):
        if department_name in self.departments:
            self.departments[department_name].add_patient(patient)
        else:
            print(f"Department '{department_name}' does not exist.")

    def retrieve_patient(self, patient_id):
        found_patient = False
        for department in self.departments.values():
            for patient in department.patients:
                if patient.patient_id == patient_id:
                    found_patient = True
                    print("Patient information for ID:", patient_id)
                    print("Gender:", patient.gender)
                    print("Race:", patient.race)
                    print("Age:", patient.age)
                    print("Ethnicity:", patient.ethnicity)
                    print("Insurance:", patient.insurance)
                    print("Zip code:", patient.zip_code)
                    print("Visits:")
                    for visit in patient.visits:
                        print("Visit ID:", visit.visit_id)
                        print("Visit time:", visit.visit_time.strftime('%Y-%m-%d'))
                        print("Department:", visit.department)
                        print("Chief complaint:", visit.chief_complaint)
                        # Additional loop to print notes for each visit
                        print("Notes:")
                        for note in patient.notes:
                            print("Note ID:", note['note_id'])
                            print("Note Type:", note['note_type'])
                    break
            if found_patient:
                break
        if not found_patient:
            print("Patient not found.")

    def remove_patient(self, patient_id):
        removed_patient = False
        for department in self.departments.values():
            for patient in department.patients:
                if patient.patient_id == patient_id:
                    department.patients.remove(patient)
                    removed_patient = True
                    break
            if removed_patient:
                break
        return removed_patient
    def count_visits_on_date(self, date):
        total_visits = 0
        for department in self.departments.values():
            for patient in department.patients:
                for visit in patient.visits:
                    if visit.visit_time.date() == date.date():
                        total_visits += 1
        return total_visits

def read_patient_data(file_path):
    hospital = Hospital()
    with open(file_path, 'r') as file:
        if file_path.lower().endswith('.csv'):
            reader = csv.DictReader(file)
            for row in reader:
                patient_id = row['Patient_ID']
                department_name = row['Visit_department']
                hospital.add_department(department_name)
                patient = Patient(patient_id, row['Gender'], row['Race'], int(row['Age']), row['Ethnicity'], row['Insurance'], row['Zip_code'])
                hospital.add_patient_to_department(department_name, patient)
                visit_id = row['Visit_ID']  # No conversion needed
                visit_time = datetime.strptime(row['Visit_time'], '%Y-%m-%d')
                chief_complaint = row['Chief_complaint']
                visit = Visit(visit_id, visit_time, department_name, chief_complaint)
                patient.add_visit(visit)
                note_id = row['Note_ID']
                note_type = row['Note_type']
                patient.add_note(note_id, note_type)

        else:
            print("Unsupported file format.")
    return hospital
