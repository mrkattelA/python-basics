import random

def rand_nums(low,high,num):
    numbers = []
    for number in range(num):
        numbers.append(random.randint(low,high))
    return numbers

randomnumbers = rand_nums(1,100,5)

print(randomnumbers)

print("First time through: ")
for number in randomnumbers:
    print(number)

print("")
print("Second time through: ")
for number in randomnumbers:
    print(number)

print("")
print("Third time through: ")
for number in randomnumbers:
    print(number)

print("")
print("Fourth time through: ")
for numberss in randomnumbers:
    print(numberss)
