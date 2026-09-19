#Different Payment Method

class Payment:
    def make_payment(self):
        return "\nPayment Done!\n"
class CreditCard(Payment):
    def make_payment(self):
        return "\nPayment done via Credit Card!\n"

class PayPal:
    def make_payment(self):
        return "\nPayment done via Pay Pal!"

class BankTransfer:
    def make_payment(self):
        return "\nPayment done via Bank Transfer!"

def pay_options():
    print("\n--- Options ---\n")
    print("[1] Credit Card")
    print("[2] Pay Pal")
    print("[3] Bank Transfer")
    print("[0] Cancel\n")

def main():
    pay = PayPal()
    card = CreditCard()
    bank = BankTransfer()
    while True:
        pay_options()
        ops = input("<?>---> ").strip()

        if ops == "1":
            card.make_payment()
        elif