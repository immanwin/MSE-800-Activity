class Bank:

    def __init__(self):
        self.name = "John"
        self.acc_no = "SA1001"
        self.balance: float = 5000.0
        self.d_money = 0.0
        self.w_money = 0.0
        


    def view_account_details(self):
        print("\n--- View Details ---\n")
        print(f"Name: {self.name}")
        print(f"Acc.No: {self.acc_no}")
        print(f"Balance: ${self.balance}")
        return self.balance

    def withdraw_money(self):
        print("\n--- Withdraw Money ---\n")
        self.w_money = float(input("<?>---> $"))
        if (self.w_money <= self.balance):
            self.balance = self.balance - self.w_money
            print(f"\nWithdrew: ${self.w_money}")
            print(f"Balance: ${self.balance}")
        else:
            print("\nSorry insufficient Balance\n")
        return self.balance

    def deposit_money(self):
        print("\n--- Deposit Money ---\n")
        self.d_money = float(input("<?>---> $"))

        self.balance = self.balance + self.d_money
        return self.balance

class SavingsAccount(Bank):

    def __init__(self):
        self.interest: float = 0.0
        super().__init__(1)

    def calculate_interest(self):
        self.interest = self.balance * 1.0 * 5 / 100
        print(f"\nCaculated Interest: ${self.interest}")

def menu():
    print("\n--- Menu ---\n")
    print("[1] View Details")
    print("[2] Withdraw Money")
    print("[3] Deposit Money")
    print("[4] Calculate Interest")
    print("[0] Exit\n")

def main():
    bank = Bank()
    sa = SavingsAccount()
    while True:
        menu()
        ops = input("<?>---> ").strip()
        if ops == "1":
            bank.view_account_details()
        elif ops == "2":
            bank.withdraw_money()
        elif ops == "3":
            bank.deposit_money()
        elif ops == "4":
            sa.calculate_interest()
        elif ops == "0":
            print("\nThank you!\n")
            break
        else:
            print("\nTry Again!\n")
        

if __name__ == "__main__":
    main()