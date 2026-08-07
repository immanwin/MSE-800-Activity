#BMI_Calculator

#Usage of Class
class Person_Health: 

    #Mehthod to Calculate the Function
    def bmi_caculation(h,w):
        bmi = w/(h**2)
        print(f"Body-Mass Index = {bmi:.2f} kg/m^2")

#Main Function
def main():

    #Getting Input for the Calculation
    height = float(input("Height (m)= "))
    weight = float(input("Weight (Kg)= "))

    #Result...
    output = Person_Health.bmi_caculation(height,weight)

#Execution...
if __name__ == "__main__":
    main()