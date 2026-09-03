#Activity-2

def act_2():
    #Key-Value-1
    keys_1 = ['a','b','c','d','f','g','h','e','a']
    values_1 = [20, 3, 1, 88, 55, 92, 6, 90, 910]

    #Key-Value-2
    keys_2 = ['u','b','o','x','e','a']
    values_2 = [200, 30, 10, 88, 55, 920]

    #Creating Dictionaries (separately for better understanding)
    dict_1 = {k:v for k,v in zip(keys_1,values_1) if v%2 != 0}
    dict_2 = {k:v for k,v in zip(keys_2,values_2) if v%2 != 0}

    #Combining/Merging Output Dictionary
    output_dict = {**dict_1, **dict_2}

    #Printing final output dictionary
    print(f"Output Dictionary: {output_dict}")
    print("\n--------------------\n")

def main():
    print("\n\n-----Activity-2-----\n")
    act_2() #Calling the Activity-2 function

if __name__ == "__main__":
    main()