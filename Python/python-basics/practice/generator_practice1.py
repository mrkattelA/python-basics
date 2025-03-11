import random

def gen_ran_num(low,high,num):
    num_list=[]
    for number in range(num):
        num_list.append(random.randint(low,high))
    return num_list

def gen_ran_num_thru_gen(low, high, num):
    for number in range(num):
        yield random.randint(low,high)

ant = 1,100,5

numbers = gen_ran_num_thru_gen(1,100,5)
print(numbers)

print("First Time Generator: ")
for num in numbers:
    print(num)

print("")
print("Second time generator: ")
for nums in gen_ran_num_thru_gen(1,100,5):
    print(nums)

print("xxx")
print(sep= " ")
print("Third time generator: ")
for num in gen_ran_num_thru_gen(ant[0],ant[1],ant[2]):
    print(num)

print("==================================")
print("Fourth time generator ")
for nun in numbers:
    print(nun)

print("""***
***
***
***
***""")
print("no value returned on fourth generator. ")
print("becase 'Generator' can be called only 1 Time. ")

def gen_ran_numbs(low, high, num):
    for numberrrs in range(num):
        yield random.randint(low,high)

n = gen_ran_numbs(1,100,5)
print("\t".format(n))
