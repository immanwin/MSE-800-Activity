# Exception Handling - 2

def my_function(a,b):
    a = a/b
    #result = a / 0     #Alternative Code Snippet, to execute Except clause
    result = a
    print(result)

try:
    my_function(6, 2)
except ZeroDivisionError as e:
    print(e)
else:
    print("Everything worked OK")
finally:
    print("Always runs")

