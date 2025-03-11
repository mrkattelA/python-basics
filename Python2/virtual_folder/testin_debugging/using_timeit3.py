import timeit
import random

str_num1 = """
numbers = str(random.randint(1,100))
for i in range(1000):
    num = random.randint(1,100)
    numbers += ',' + str(num)"""

str_num2 = """
numbers = [str(random.randit(1,100) for i in range(1000))]
numbers = ','.join(numbers)"""

td1 = timeit.timeit(str_num1, number=1000, globals=globals())
td2 = timeit.timeit(str_num2, number=1000, globals=globals())

print("Results from using repeat()")
print(td1, td2, sep="\n")
print('-' * 70)

print('str_nums1 compared to str_nums2:')
print(f"{td1/td2:.2%}")