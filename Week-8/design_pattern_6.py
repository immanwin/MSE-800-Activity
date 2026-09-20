#Structural Patterns (Adapter)

class Target:
    def pay(self):
        pass

class Adaptee:
    def make_payment(self):
        print("$500 Payment Successful!")

class Adapter (Target):
    def __init__(self,adaptee):
        self.adaptee = adaptee

    def pay(self):
        self.adaptee.make_payment()

adaptee = Adaptee()
adapter = Adapter(adaptee)
adapter.pay()