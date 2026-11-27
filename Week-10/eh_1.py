# Exception Handling - 1


text = "xyz"
value = "0"

try:
    value = int(text)
    result = 100 / value
except ValueError:
    print("Not a number")
except ZeroDivisionError:
    print("Cannot divide by zero")
