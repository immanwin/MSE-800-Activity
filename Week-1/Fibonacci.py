#Fibonacci Series

def Factorial(n):
    next_num = 1
    starting_num = 0
    previous_num = starting_num

    print(f"Fibo: {starting_num}")
    print(f"Fibo: {next_num}")
    for i in range(1,n+1):
        fibo = previous_num + next_num
        print(f"Fibo: {fibo}")
        previous_num = next_num
        next_num = fibo

Number = int(input("Enter the Number = "))
Factorial(Number)