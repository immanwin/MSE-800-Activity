#BMI_Calculator

#Usage of Class
class Person_Health: 

    #Mehthod to Calculate the Function
    def bmi_caculation(height,weight):
        bmi = weight/(height**2)
        print(f"\nBody-Mass Index = {bmi:.2f} kg/m^2\n")

        #Categorize the BMI-Level
        if (bmi < 18.50): #Under-Weight
            print("Result: Under-Weight")
        elif (bmi >= 18.50 and bmi <= 24.99): #Normal
            print("Result: Normal")
        elif (bmi >= 25.00 and bmi <= 29.99): #Overweight
            print("Result: Overweight")
        elif (bmi >= 30.00 and bmi <= 34.99): #Obese
            print("Result: Obese")
        else: #Extreme Obese
            print("Result: Extreme Obese")


        

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