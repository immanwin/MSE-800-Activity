def actions (og):
    def wrapper():
        auth = og()
        if (auth):
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

            return view_salary, view_personal_details, download_report

    return wrapper

@actions
def login_required():
    user = input("Username: ").strip()
    pwd = input("Password: ").strip()

    login = False

    if user == "imman" and pwd == "1234":
        login = True
        print("\nWelcome Imman,\n")
    else:
        print("\nAccess Denied\n")
    return login

def menu():
    print("\nMenu")
    print("[1] View Salary")
    print("[2] View Personal Details")
    print("[3] Download Report")
    print("[0] Exit\n")

def main():
    funcs = login_required()
    if funcs:
        salary_func, details_func, report_func = funcs
        while True:
            menu()
            ops = input("<?>---> ").strip()

            if (ops == "1"):
                salary_func()
            elif (ops == "2"):
                details_func()
            elif (ops == "3"):
                report_func()
            elif (ops == "0"):
                print("\nThank You!\n")
                break
            else:
                print("\nInvalid Response...\n")


if __name__ == "__main__":
    main()