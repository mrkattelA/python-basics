def addition(num1, num2):
    total = num1 + num2
    print("The addition of ", num1, " and ", num2, " is ", total, ".", sep="")

def main():
    #addition(45,35)
    #addition(1.1, 2)
   num3 = input("Enter the first number: ")
   num4 = input("Enter the second number: ")
   addition(num3, num4)
   addition(1.1,4)

main()