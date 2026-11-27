# Exception Handling - 5

try:
    print("A")
    x = int("abc")
    print("B")
except ValueError:
    print("C")
finally:
    print("D")
