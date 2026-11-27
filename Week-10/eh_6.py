


def f():
    try:
        return "try"
    finally:
        print("cleanup")
 
print(f())
