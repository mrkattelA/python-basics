import math


def pizza():
    person = int(input("How many people are you? "))
    slice = float(input("How many slices each person will eat? "))
    total = person*slice
    #print(total)
    pizza = math.ceil(total/8)
    #leftover = abs(pizza)*8-total
    #print("no of pizza is ", pizza, "and the leftover is ", leftover, end="")
    leftover = pizza*8-total
    print(person, " people  who can have ", slice, " each, needs to order ", pizza, " pizza, then the leftover will be ", leftover, sep="" )

def main():
    pizza()

main()