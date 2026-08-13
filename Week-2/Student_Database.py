#Student Database

class Student_Database:

    def __init__(self):
        self.student_data = []

    def getStudentCount(self):
        self.count = int(input("No of Students = "))
        return self.count

    def getStudentData(self):
        print("\n")
        self.name = input("Name: ").strip()
        self.age = int(input("Age: ").strip())
        self.address = input("Address: ")
        self.student_id = int(input("Student ID: ").strip())

        self.student_data.append([self.name,self.age,self.address,self.student_id])
        return self.student_data
    def printStudentData(self):
        sorted_list = self.student_data.sort(key= lambda x: x[1])
        for i in self.student_data:
            print(i)

def main():
    print("Student DataBase")
    print("~~~~~~~~~~~~~~~~\n")

    output = Student_Database()
    count = output.getStudentCount()
    for i in range(0,count):
        output.getStudentData()
    print("\n\nThe Data~")
    output.printStudentData()

    

if __name__ == "__main__":
    main()