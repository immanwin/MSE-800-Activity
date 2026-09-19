# class InfinityGauntlet:

#     def stone(self):
#         return "\nSnap!\n"

# class Power(InfinityGauntlet):

#     def stone(self):
#         return "\nPower!\n"

# class Time(InfinityGauntlet):

#     def stone(self):
#         return "\nTime!\n"
# def main():
#     marvel = [Power(), Time(), InfinityGauntlet()]
#     for i in marvel:
#         print(i.stone())

# if __name__ == "__main__":
#     main()

from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass
# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")
# class Cat(Animal):

#     def sound(self):
#         print("Cat meows")

class ATM (ABC):

    @abstractmethod
    def insert_card(self):
        pass

class BankATM(ATM):
    def __init__(self):
        self.balance = 5000.0
        self.w_money = 0.0
        
    def insert_card(self):
        print("Insert Card...")

    def enter_pin(self):
        self.pin = int(input("PIN: "))
        return self.pin

    def check_balance(self):
        print(f"Balance = {self.balance}")

    def withdraw_money(self):
        self.w_money = float(input("$: "))
        self.balance -= self.w_money

        # print(f"\nBalance: ${self.balance}")
        return self.balance

bank = BankATM()
bank.insert_card()
bank.enter_pin()
bank.check_balance()
bank.withdraw_money()
bank.check_balance()