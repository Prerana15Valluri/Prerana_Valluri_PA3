import csv

class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

def read_credentials(file_path):
    users = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            user = User(row['username'], row['password'], row['role'])
            users.append(user)
    return users

def authenticate_user(username, password, users):
    for user in users:
        if user.username == username and user.password == password:
            return user
    return None
