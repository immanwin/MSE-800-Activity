#Main Program

from database import create_table
from management import view_transactions, add_transaction

class ExchangeMoney:

    def __init__(self):
        self.s_amount = 0.0
        self.cf = 0
        self.r_amount = 0.0

    #Title of the Program
    def head(self):
        print("\n=== Exchange Money App ===\n\n")

    #Basic Menu
    def menu(self):
        print("\n--- Menu ---\n")
        print("[1] Login")
        print("[2] View Transactions")
        print("[0] Exit\n")

    #Sender Info
    def sender_info(self):
        print("\n--- Sender Info ---\n")
        self.username = input("User-Name: ")
        self.bank_id = int(input("Bank-ID: "))
        return self.username, self.bank_id
    #Receiver Info
    def receiver_info(self):
        print("\n--- Receiver Info ---\n")
        self.r_name = input("User-Name: ")
        self.r_bid = int(input("Bank-ID: "))
        return self.r_name, self.r_bid

    #Sender Info
    def sender_currency(self):
        print("\n--- Sender Currency ---\n")
        print(f"Welcome {self.username}, choose the Currency:")
        print("[1] NZD")
        print("[2] INR\n")
        self.s_currency = int(input("<?>--> "))
        return self.s_currency

    #Receiver Info
    def receiver_currency(self):
        print("\n--- Receiver Currency ---\n")
        print(f"Choose Receiver: {self.r_name}'s Currency:")
        print("[1] NZD")
        print("[2] INR\n")
        self.r_currency = int(input("<?>--> "))
        return self.r_currency

    def nzd_inr(self):
        self.cf = 57.18
        self.r_amount = self.cf * self.s_amount
        return self.r_amount
    
    def inr_nzd(self):
        self.cf = 0.01749
        self.r_amount = self.cf * self.s_amount
        return self.r_amount
    
    def same_currency(self):
        self.r_amount = self.s_amount
        return self.r_amount

    def ask_money(self):
        print("\n--- Sender Money ---\n")
        if self.s_currency == 1:
            self.s_amount = float(input("<?>--> $ "))
        elif self.s_currency == 2:
            self.s_amount = float(input("<?>--> Rs. "))
        else:
            print("\nOops!: Invalid Response...\n")
        return self.s_amount

    def transaction(self):
        if (self.s_currency == self.r_currency):
            self.same_currency()
        elif (self.s_currency == 1 and self.r_currency == 2):
            self.nzd_inr()
        elif (self.s_currency == 2 and self.r_currency == 1):
            self.inr_nzd()

    def sent_money(self):
        print("\n--- Money Sent ---\n")
        
        if (self.r_currency == 1):
            print(f"Successfully Sent $ {self.r_amount} to {self.r_name}")
        else:
            print(f"Successfully Sent Rs. {self.r_amount} to {self.r_name}")

def main():
    create_table()
    em = ExchangeMoney()
    em.head()
    while True:
        em.menu()
        ops = int(input("<?>--> "))
        if (ops == 0): #Exit
            print("\nThank You!")
            break
        elif (ops == 1): #Login Page
            em.sender_info()
            em.receiver_info()
            em.sender_currency()
            em.receiver_currency()
            em.ask_money()
            em.transaction()
            em.sent_money()

            add_transaction(
                em.username, em.bank_id, em.r_name, em.r_bid, em.s_amount, em.r_amount
            )

        elif (ops == 2):
            transactions = view_transactions()
            for trans in transactions:
                print(trans)
            print("\n\n")
        else: #Invalid Response
            print("\nOops!: Invalid Response...\n")

if __name__ == "__main__":
    main()
