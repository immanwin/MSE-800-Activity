class Score:
    def __init__(self):
        self.mark_list = []
        self.name_list = []
        self.status = []
    def student_details(self):
        self.name = input("Name: ").strip()
        self.mark = float(input("Mark = "))
        self.name_list.append(self.name)
        self.mark_list.append(self.mark)
        if (self.mark >= 50):
            self.status.append("Pass")
        else:
            self.status.append("Fail")
        return self.name_list, self.mark_list

    def class_avg(self):
        self.avg = sum(self.mark_list)/len(self.mark_list)
        print(f"Class Average = {self.avg}")

    def student_result(self):
        print("\n---Student - Results---\n")
        for i in range(len(self.name_list)):
            print(f"{i+1}. {self.name_list[i]} ---> {self.status[i]}")

    def highest_mark(self):
        h_mark = self.mark_list.index(max(self.mark_list))
        print(f"Highest Mark is {self.mark_list[h_mark]} scored by {self.name_list[h_mark]}")


def main():
    print("=== STUDENT REPORT ===")
    work = Score()
    print("\n---Student Mark Entry---")
    for i in range(2):
        work.student_details()
        print("\n")
    work.student_result()
    print("\n")
    work.class_avg()
    print("\n")
    work.highest_mark()

if __name__ == "__main__":
    main()

