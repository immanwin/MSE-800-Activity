#Excercise-1: Find the Average

def Average(t1,t2,t3):
    avg = (t1+t2+t3)/3
    print(f"The Average = {avg}")

test_1 = float(input("Test-1: "))
test_2 = float(input("Test-2: "))
test_3 = float(input("Test-3: "))

Average(test_1,test_2,test_3)