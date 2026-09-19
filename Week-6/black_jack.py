# #decorator functions

# def my_decor (original_function):
#     def wrapper():
#         print("Line-2")
#         original_function()
#         print("Line-3")
#     return wrapper
# @my_decor
# def mid_line():
#     print("Line-1")

# mid_line()

# print("\n\n\n")

# def square(func):
#     def wrapper(a,b):
#         result = func(a,b)
#         print(f"Results: {result}")
#         return result
#     return wrapper
# @square
# def numbers(a,b):
#     return a**2, b**2
# numbers(2,3)
# az

def login_required(function1,function2,function3):
    def wrapper():
        login = False
        username = input("username: ")
        password = input("Password: ")

        if username == "imman" and password == "1234":
            login = True
            print("Welcome Imman,")
            print("\nMenu")
            print("[1] View Salary")
            print("[2] View Personal Details")
            print("[3] Download Report")
            print("[0] Exit\n")

            while True:

                ops = int(input("<?>---> "))
                if ops == 1:
                    function1()
                elif ops == 2:
                    function2()
                elif ops == 3:
                    function3()
                elif ops == 0:
                    break
        else:
            print("\nAccess Denied!\n")
        return wrapper

@login_required
def view_salary():
    print("\nSalary = $ 150,000 per year\n")

    
def view_personal_details():
    print("\nEmployee Details:\n")
    print("Imman")
    print("MSE-800")
    print("@Yoobee\n")


def download_report():
    print("\nDownloading Report...")
    print("100% Complete!")

view_salary()
view_personal_details()
download_report()