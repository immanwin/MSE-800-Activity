class Department:
    def __init__(self):
        self.head = "Mr. Regis"
        self.name = "MECH"
    def show_department(self):
        print(f"\nDept-Name: {self.name}")
        print(f"Dept-Head: {self.head}")

class University(Department):
    def __init__(self):
        self.university_name = "LICET"
        self.department = Department()

    def show_university(self):
        print(f"University: {self.university_name}")
        self.department.show_department()

uni = University()
uni.show_university()