#Problem-2: BMI Calculator

height = float(input("Height (m)= "))
weight = float(input("Weight (Kg)= "))

bmi = weight/(height**2)

print(f"Height: {height}m")
print(f"Weight: {weight}Kg")
print(f"Body-Mass-Index = {bmi:.2f} m/kg^2")