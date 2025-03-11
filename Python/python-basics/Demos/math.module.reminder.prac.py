def divide(num1,num2):
    answer = num1/num2
    print("the division of ", num1 , " by ", num2 , " is ", answer, "." ,sep="")

def divide_reminder(num3,num4):
    division = num3/num4
    floor = num3//num4
    module = num3%num4
    print(num3, " divided by ", num4, " equals ", floor, " with a reminder of ", module, ".", sep="")

# 5 divided by 2 equals 2 with a remainder of 1

def main():
    divide(8,2)
    divide(5,2)
    divide_reminder(8,2)
    divide_reminder(5,2)
    divide_reminder(11,3)
    divide_reminder(17,5)
    divide_reminder(15,8)
    divide_reminder(10,2)

main()