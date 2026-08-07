#Problem-2: BMI Calculator
def main():
    height = float(input("Height (m)= "))
    weight = float(input("Weight (Kg)= "))
    BMI_Calculator (weight,height)
def BMI_Calculator(weight,height):
    bmi = weight/(height**2)
    print(f"Body-Mass-Index = {bmi:.2f} m/kg^2")

if __name__ == "__main__":
    main()