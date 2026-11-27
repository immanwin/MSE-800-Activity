#Failing Code

def show_car_details():
    print("\nCar-Details:")
    print("Make: Audi")
    print("Model: r8")
    print("Fee/Day: $2500")
    print("\nCan you confirm Booking?")

def calculate_fee(d):
    if d >= 7:
        discount = 2500 - (2500*10/100)
        fare = d * discount
    else:
        fare = d * 2500
    
    print(f"Total Fare: ${fare}")
    return fare



def main():
    print("\nBooking System\n")
    show_car_details()
    confirm_1 = input("<?>--> [y/n]: ").strip()

    if(confirm_1 == "y"):

        days = int(input("How many days?: "))
        calculate_fee(days)

        print("\n\n\n")
        print("The program runs with error... (Red Test)")
    
if __name__ == "__main__":
    main()