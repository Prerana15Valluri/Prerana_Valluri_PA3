from hospital import Patient
from datetime import datetime, timedelta
from collections import defaultdict


def remove_patient_action(hospital):
    patient_id = input("Enter Patient_ID: ")
    removed_patient = hospital.remove_patient(patient_id)
    if removed_patient:
        print("Patient removed successfully.")
    else:
        print("Patient not found.")

def count_visits_action(hospital):
    date_str = input("Enter date (YYYY-MM-DD): ")
    try:
        date = datetime.strptime(date_str, '%Y-%m-%d')
        total_visits = hospital.count_visits_on_date(date)
        print("Total visits on", date.strftime('%Y-%m-%d'), ":", total_visits)
    except ValueError:
        print("Invalid date format.")


def retrieve_patient_action(hospital):
    patient_id = input("Enter Patient_ID: ")
    hospital.retrieve_patient(patient_id)

def perform_admin_actions(hospital):
    action = input("Choose an action (count_visits): ").strip().lower()
    if action == 'count_visits':
        date_str = input("Enter date (YYYY-MM-DD): ")
        try:
            date = datetime.strptime(date_str, '%Y-%m-%d')
            total_visits = hospital.count_visits_on_date(date)
            print("Total visits on", date.strftime('%Y-%m-%d'), ":", total_visits)
        except ValueError:
            print("Invalid date format.")

def perform_clinician_nurse_actions(hospital):
    while True:
        action = input("Choose an action (add_patient, remove_patient, retrieve_patient, count_visits, stop): ").strip().lower()

        if action == "stop":
            break
        elif action == "add_patient":
            add_patient_action(hospital)
        elif action == "remove_patient":
            remove_patient_action(hospital)
        elif action == "retrieve_patient":
            retrieve_patient_action(hospital)
        elif action == "count_visits":
            count_visits_action(hospital)
        else:
            print("Invalid action.")

def add_patient_action(hospital):
    patient_id = input("Enter Patient_ID: ")
    department_name = input("Enter department name: ")
    gender = input("Enter Gender: ")
    race = input("Enter Race: ")
    age = int(input("Enter Age: "))
    ethnicity = input("Enter Ethnicity: ")
    insurance = input("Enter Insurance: ")
    zip_code = input("Enter Zip code: ")
    
    # Check if department exists, if not, add it
    if department_name not in hospital.departments:
        hospital.add_department(department_name)
        print(f"Department '{department_name}' added.")

    patient = Patient(patient_id, gender, race, age, ethnicity, insurance, zip_code)
    hospital.add_patient_to_department(department_name, patient)
    print("Patient added successfully.")

def generate_statistics_report(hospital):
    print("You have management role. Generating key statistics report...")

    # Initialize dictionaries to store counts
    visits_by_insurance = defaultdict(int)
    visits_by_race = defaultdict(int)
    visits_by_gender = defaultdict(int)
    visits_by_ethnicity = defaultdict(int)

    # Initialize dictionaries to store temporal trends
    daily_visits = defaultdict(int)
    weekly_visits = defaultdict(int)
    monthly_visits = defaultdict(int)

    # Iterate through departments and patients to collect data
    for department in hospital.departments.values():
        for patient in department.patients:
            for visit in patient.visits:
                # Count visits by insurance, race, gender, and ethnicity
                visits_by_insurance[patient.insurance] += 1
                visits_by_race[patient.race] += 1
                visits_by_gender[patient.gender] += 1
                visits_by_ethnicity[patient.ethnicity] += 1

                # Update temporal trends
                update_temporal_trends(daily_visits, visit.visit_time.date(), 1)
                update_temporal_trends(weekly_visits, get_week_start_date(visit.visit_time), 1)
                update_temporal_trends(monthly_visits, get_month_start_date(visit.visit_time), 1)

    # Print statistics for each category
    print("\n1. Temporal trend of the number of patients who visited the hospital with different types of insurances:")
    print_statistics(visits_by_insurance)

    print("\n2. Temporal trend of the number of patients who visited the hospital in different demographics groups:")
    print("  - Race:")
    print_statistics(visits_by_race)
    print("  - Gender:")
    print_statistics(visits_by_gender)
    print("  - Ethnicity:")
    print_statistics(visits_by_ethnicity)

    print("\n3. Temporal trend of the number of patients who visited the hospital over time intervals:")
    print("  - Daily trend:")
    print_temporal_trend(daily_visits)
    print("  - Weekly trend:")
    print_temporal_trend(weekly_visits)
    print("  - Monthly trend:")
    print_temporal_trend(monthly_visits)

def update_temporal_trends(trend_dict, date, count):
    trend_dict[date] += count

def get_week_start_date(date):
    return date - timedelta(days=date.weekday())

def get_month_start_date(date):
    return date.replace(day=1)

def print_statistics(data):
    for key, value in sorted(data.items()):
        print(f"{key}: {value}")

def print_temporal_trend(data):
    print("{:<12} {:<10}".format("Date", "Visits"))
    for date, visits in sorted(data.items()):
        print("{:<12} {:<10}".format(date.strftime('%Y-%m-%d'), visits))


