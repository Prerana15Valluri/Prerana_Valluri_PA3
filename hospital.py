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
