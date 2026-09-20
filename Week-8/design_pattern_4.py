#Builder Pattern

class Travel:
    def __init__(self, destination, hotel, transport, meal, activities, insurance):
        self. destination = destination
        self. hotel = hotel
        self. transport = transport
        self. meal = meal
        self. activities = activities
        self. insurance = insurance

    def show_travel(self):
        print(f"Destination: {self.destination}")
        print(f"Hotel: {self.hotel}")
        print(f"Transport: {self.transport}")
        print(f"Meal Plan: {self.meal}")
        print(f"Activites: {self.activities}")
        print(f"Insurance: {self.insurance}")

class TravelPlanner:
    def __init__(self):
        self. destination = None
        self. hotel = None
        self. transport = None
        self. meal = None
        self. activities = None
        self. insurance = None

    def set_destination(self,destination):
        self.destination = destination
        return self
    def set_hotel(self, hotel):
        self.hotel = hotel
        return self
    def set_transport(self,transport):
        self.transport = transport
        return self
    def set_meal(self,meal):
        self.meal = meal
        return self
    def set_activities(self,activities):
        self.activities = activities
        return self
    def set_insurance(self,insurance):
        self.insurance = insurance
        return self
    def plan_travel(self):
        return Travel(
            self.destination,
            self.hotel,
            self.transport,
            self.meal,
            self.activities,
            self.insurance
        )

def main():
    travel = (
        TravelPlanner()
        .set_destination("Auckland")
        .set_hotel("5-Star")
        .set_transport("Flight")
        .set_meal("Full Board")
        .set_activities("Adventure Tour")
        .set_insurance("Yes")
    )

if __name__ == "__main__":
    main()