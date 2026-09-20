#Behavioral Patterns (Observer)

class Observer:
    def update(self, price):
        pass

class Investor:
    def __init__(self, name):
        self.name = name

    def update(self):
        print(f"{self.name} received a notification!")


class Subject:
    def __init__(self):
        self.observers = []

    def attach(self,observer):
        self.observers.append(observer)

    def notify(self):
        for observer in self.observers:
            observer.update()

class StockMarket(Subject):
    def price_change(self,new_price):
        print(f"New Price: ${new_price}")
        self.notify()

def main():
    #Creating a Subject
    market = StockMarket()

    #Creating Observers
    imman = Investor("Imman")
    mukesh = Investor("Mukesh")

    #Listing the Investors
    market.attach(imman)
    market.attach(mukesh)

    #Changing Market Price
    market.price_change(500)

if __name__ == "__main__":
    main()