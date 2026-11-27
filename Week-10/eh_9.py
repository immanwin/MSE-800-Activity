#Exception Handling - Part - B

def read_int(prompt, maximum, minimum):
    run = True
    while (run):
        try:
            number = int(input(f"{prompt}"))
            if (number>=minimum) and (number<=maximum):
                print("Good Job!")
                run = False
        except ValueError:
            pass
    print("The program works...")

read_int ("Please enter a whole number = ", 10, 0)
