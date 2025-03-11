import random
from timeit import timeit

def string_num1():
    numbers = str(random.randint(1,100))
    for i in range(1000):
        num = random.randint(1,100)
        numbers += "," + str(num)

def string_num2():
    numbers = [str(random.randint(1,100) for i in range(1000))]
    numbers = ",".join(numbers)

td1 = timeit(string_num1, number=1000)
td2 = timeit(string_num2, number=1000)

print("Results from using timeit()")
print(td1, td2, sep="\n")
print("-"*70)

print("string_num1 compared to string_num2: ")
print(f"{td1/td2:.2%}")