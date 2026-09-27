import pdb


def calculate_average(a, b, c):
    total = a + b + c
    average = total / 3
    return average

x=10

result = calculate_average(60, 70, 80)
pdb.set_trace()
print("Average:", result)
