def square():
    try:
        num = int(input("Please Enter the number: "))
    except ValueError:
        print("Pleaes Enter Inegers only. ")
        square()
    else:
        print(num, " Square is ", num**2)

def cube():
    num = input("Please enter the number: ")
    if num.isdigit():
        print(num, " Cube is", int(num)**3)
    else:
        print("This is not an Integer. ")
        

def main():
    square()
    cube()

main()