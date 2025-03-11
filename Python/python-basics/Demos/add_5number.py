def addition_5number(num1,num2,num3=0,num4=0,num5=0):
    total = num1 + num2 + num3 + num4 + num5
    print("The sum of ", num1, "+", num2, "+", num3, "+", num4, "+", num5, " is ", total)

def main():
    addition_5number(1,2)
    addition_5number(1,2,3)
    addition_5number(1,2,3,4)
    addition_5number(1,2,3,4,5)

main()