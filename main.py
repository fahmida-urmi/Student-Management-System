from entities.student import Student
from entities.course import Course
from lib.file_operations import save_data, load_data



students = {}
courses = {}

# CLI functions for each option
def add_student():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    address = input("Enter Address: ")
    student_id = input("Enter Student ID: ")
    student = Student(name, age, address, student_id)
    students[student_id] = student
    print(f"Student {name} (ID: {student_id}) added successfully.")

def add_course():
    course_name = input("Enter Course Name: ")
    course_code = input("Enter Course Code: ")
    instructor = input("Enter Instructor Name: ")
    course = Course(course_name, course_code, instructor)
    courses[course_code] = course
    print(f"Course {course_name} (Code: {course_code}) created with instructor {instructor}.")

def enroll_student_in_course():
    student_id = input("Enter Student ID: ")
    course_code = input("Enter Course Code: ")
    if student_id in students and course_code in courses:
        student = students[student_id]
        course = courses[course_code]
        student.enroll_course(course.course_name)
        course.add_student(student)
        print(f"Student {student.name} (ID: {student_id}) enrolled in {course.course_name} (Code: {course_code}).")
    else:
        print("Student ID or Course Code not found.")

def add_grade_for_student():
    student_id = input("Enter Student ID: ")
    course_code = input("Enter Course Code: ")
    grade = input("Enter Grade: ")
    if student_id in students and course_code in courses:
        student = students[student_id]
        if courses[course_code].course_name in student.courses:
            student.add_grade(courses[course_code].course_name, grade)
            print(f"Grade {grade} added for {student.name} in {courses[course_code].course_name}.")
        else:
            print("Student not enrolled in the course.")
    else:
        print("Student ID or Course Code not found.")

def display_student_details():
    student_id = input("Enter Student ID: ")
    if student_id in students:
        students[student_id].display_student_info()
    else:
        print("Student not found.")

def display_course_details():
    course_code = input("Enter Course Code: ")
    if course_code in courses:
        courses[course_code].display_course_info()
    else:
        print("Course not found.")

# Main menu function
def main_menu():
    while True:
        print("==== Student Management System ====")
        print("1. Add New Student")
        print("2. Add New Course")
        print("3. Enroll Student in Course")
        print("4. Add Grade for Student")
        print("5. Display Student Details")
        print("6. Display Course Details")
        print("7. Save Data to File")
        print("8. Load Data from File")
        print("0. Exit")
        choice = input("Select Option: ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            add_course()
        elif choice == "3":
            enroll_student_in_course()
        elif choice == "4":
            add_grade_for_student()
        elif choice == "5":
            display_student_details()
        elif choice == "6":
            display_course_details()
        elif choice == "7":
            save_data(students, courses)
        elif choice == "8":
            data = load_data()
            if data:
                pass
        elif choice == "0":
            print("Exiting Student Management System. Goodbye!")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main_menu()
