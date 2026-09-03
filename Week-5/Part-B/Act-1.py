#Week-5 (Class Activity)

def main_method():
    print("\n\n-----Activity-1-----\n")
    #Initial Values for Keys & Values
    keys_1 = ["a","b","c"]
    values_1 = [1,2,3]

    #Dictionary-1
    dict_1 = {k:v for k,v in zip(keys_1,values_1)}

    #Displaying the newly built Dictionary
    print(f"Dictionary: {dict_1}")
    print("\n--------------------\n")

def diff_method(): #Same Values & Keys but different method
    print("\n\n-----Activity-1 (Other Method)-----\n")
    
    keys_1 = ["a","b","c"]
    values_1 = [1,2,3]

    #Dictionary-1
    dict_1 = dict(zip(keys_1,values_1))

    #Displaying the newly built Dictionary
    print(f"Dictionary: {dict_1}")
    print("\n--------------------\n")

def main():
    main_method()
    diff_method()

    

if __name__ == "__main__":
    main()