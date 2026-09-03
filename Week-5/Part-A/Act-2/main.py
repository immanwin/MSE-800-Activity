# College Management App

from database import create_table
from management import add_student, view_students, delete_student

class College:
    def __init__(self):
        self.course_catalog = {
            "1": {"name": "Science", "lecturer": "Hank"},
            "2": {"name": "History", "lecturer": "Xavier"},
            "3": {"name": "Magic", "lecturer": "Stephen"},
            "4": {"name": "Gym", "lecturer": "Bruce"}
        }

    def title(self):
        print("\n===== YOOBEE =====\n")

    def menu(self):
        print("\n----- Menu -----")
        print("[1] View Student List")
        print("[2] Add Student")
        print("[3] Delete Student")
        print("[0] Exit\n")

    def select_courses(self):
        print("\nAvailable Courses:")
        for key, details in self.course_catalog.items():
            print(f"[{key}] {details['name']} (Lecturer: {details['lecturer']})")

        selections = input("Enter course numbers to enroll (comma-separated, e.g., 1,3): ").split(",")
        enrolled = []
        for s in selections:
            s = s.strip()
            if s in self.course_catalog:
                course = self.course_catalog[s]
                enrolled.append(f"{course['name']} ({course['lecturer']})")

        return ", ".join(enrolled) if enrolled else "No courses selected"

def main():
    create_table()
    work = College()
    work.title()

    while True:
        work.menu()
        ops = input("<?>---> ").strip()

        #View Students
        if ops == "1":
            students = view_students()
            print("\n--- Registered Students ---")
            if not students:
                print("\nNo students found.\n")
            else:
                for s_id, name, courses in students:
                    print(f"ID: {s_id} | Name: {name} | Enrolled: {courses}")
                print()

        #Add Students
        elif ops == "2":
            print("\n--- Add Students ---")
            name = input("Name: ").strip()
            if not name:
                print("\nName cannot be empty.\n")
                continue
            courses = work.select_courses()
            add_student(name, courses)

        #Delete Students
        elif ops == "3":
            raw_id = input("ID: ").strip()
            if raw_id.isdigit():
                delete_student(int(raw_id))
            else:
                print("\nInvalid ID. Please enter a number.\n")

        #Exit
        elif ops == "0":
            print("\nThank You!\n")
            break

        #Invalid Response ...
        else:
            print("\nInvalid Response: Try Again ...\n")

if __name__ == "__main__":
    main()