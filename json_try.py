import json

students = {
    101: {"name": "Sarthak", "age": 20, "course": "IT"},
    102: {"name": "Mishi", "age": 21, "course": "CSE"},
    103: {"name": "manyu", "age": 19, "course": "ECE"}}


with open("student_data.json", "w") as fh:
    json.dump(students, fh, indent=4)