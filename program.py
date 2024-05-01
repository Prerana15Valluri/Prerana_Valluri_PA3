from credentials_manage import read_credentials, authenticate_user
from hospital_management import perform_admin_actions, perform_clinician_nurse_actions, generate_statistics_report
from healthcare_system import read_patient_data

class Program:
    def __init__(self, credentials_file, patients_file):
        self.credentials_file = credentials_file
        self.patients_file = patients_file

    def start(self):
        # Load hospital data
        hospital = read_patient_data(self.patients_file)

        # Load user credentials
        users = read_credentials(self.credentials_file)

        authenticated_user = None
        while authenticated_user is None:
            username = input("Enter username: ")
            password = input("Enter password: ")
            authenticated_user = authenticate_user(username, password, users)
            if authenticated_user is None:
                print("Invalid credentials. Please try again.")

        if authenticated_user.role == 'admin':
            print("You have admin role. You can perform count_visits.")
            perform_admin_actions(hospital)
        elif authenticated_user.role in ['clinician', 'nurse']:
            print("You have clinician/nurse role.")
            perform_clinician_nurse_actions(hospital)
        elif authenticated_user.role == 'management':
            generate_statistics_report(hospital)
