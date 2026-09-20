#Different Food

class Pizza:
    def prepare(self):
        print("Order: Pizza is preparing...")
class Burger:
    def prepare(self):
        print("Order: Burger is preparing...")
class Pasta:
    def prepare(self):
        print("Order: Pasta is preparing...")

class PrepareFood:

    @staticmethod
    def prepare_food(food):
        if food == "pizza":
            return Pizza()
        elif food == "burger":
            return Burger()
        elif food == "pasta":
            return Pasta()
        else:
            raise ValueError ("Invalid Food Order")

order = PrepareFood.prepare_food("pasta")
order.prepare()
