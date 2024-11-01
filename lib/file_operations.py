import json
import os

def save_data(students, courses):
    os.makedirs("data", exist_ok=True)
    data = {
        "students": {sid: {"name": s.name, "age": s.age, "address": s.address, "student_id": s.student_id,
                           "grades": s.grades, "courses": s.courses} for sid, s in students.items()},
        "courses": {cid: {"course_name": c.course_name, "course_code": c.course_code, "instructor": c.instructor,
                          "students": [s.student_id for s in c.students]} for cid, c in courses.items()}
    }
    with open("data/student_data.json", "w") as f:
        json.dump(data, f)
    print("All student and course data saved successfully.")

def load_data():
    try:
        with open("data/student_data.json", "r") as f:
            data = f.readlines()
        # Load and process data as needed
        print("Data loaded successfully.")
        return data
    except FileNotFoundError:
        print("No saved data found.")
        return None
