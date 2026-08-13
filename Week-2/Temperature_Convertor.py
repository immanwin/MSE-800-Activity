#Integration of Class
class Temperature:

    #Creating Constructor Method
    def __init__(self):
        self.temp = 0.0
        self.unit = ""       

    #Method to Input Temperature
    def get_temperature(self):
        self.input_temp = input("Enter Temperature: ").strip()
        return self.input_temp
    
    #Method to Check the format of the Input Temperature
    def checking_format(self):

        #Checking the Prefix
        if (self.input_temp[0] in ("C","F")): 

            #Storing the Temperature Value
            self.temp: float = float(self.input_temp[1:])

            #Storing the Current Temperature Unit
            self.unit: str = self.input_temp[0] 

            return self.temp, self.unit

        #Displays when the Input is Incorrect
        else: 
            print("Invalid Input: Please enter the temperature with the correct 'C' or 'F' prefix")

    #Method to print the Output (Along with Calculation/Conversions)
    def output_temperature(self):

        #Converting to Fahrenheit
        if (self.unit == "C"):
            self.output_temp = (self.temp * (9/5) + 32)
            print(f"C{self.temp:.2f} = F{self.output_temp:.2f}")

        #Converting to Celcius
        elif (self.unit == "F"):
            self.output_temp = (self.temp - 32) * (5/9)
            print(f"C{self.temp:.2f} = F{self.output_temp:.2f}")

#Main Program
def main():
    #Creating object called 'working'
    working = Temperature()

    #Invoking methods via class-objects
    working.get_temperature()
    working.checking_format()
    working.output_temperature()

#Executing Main Program...
if __name__ == "__main__":
    main()
