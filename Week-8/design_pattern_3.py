#Singleton Design Pattern

class UniversityConfig:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.uni_name = "LICET"
            cls._instance.acd_year = "2025"
            cls._instance.semester = "8"

        return cls._instance

def main():
    #Creating 3 Objects
    student_1 = UniversityConfig()
    student_2 = UniversityConfig()
    student_3 = UniversityConfig()

    #The Pre-defined Contents
    print("\nPre-Defined:")
    print("````````````")
    print(f"University Name: {student_1.uni_name}")
    print(f"Academic Year: {student_1.acd_year}")
    print(f"Semester: {student_1.semester}")

    #Changing the Contents
    student_2.uni_name = "Yoobee"
    student_2.acd_year = "2026"
    student_2.semester = "1"

    #Printing the Changed contents
    print("\nNew-Defined:")
    print("````````````")
    print(f"University Name: {student_2.uni_name}")
    print(f"Academic Year: {student_2.acd_year}")
    print(f"Semester: {student_2.semester}")

    #Checking the within Objects
    print("\nChecking the Object Values:")
    print("````````````````````````````")
    print(f"Have all the Objects changed?: {student_2 is student_3}")

if __name__ == "__main__":
    main()
    