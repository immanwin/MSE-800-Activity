#Factorial of a Number

def Factorial(n):
    fact = 1
    og_n = n
    while (n!=0):
        fact = fact * n
        n-=1
    print(f"Factorial of {og_n}! is {fact}")

num = int(input("Enter a Number = "))
Factorial(num)