def divide():
    try:
        numerator = int(input("Please enter the 1st Number: "))
        denominator = int(input("Please enter the 2nd Number: "))
        result = numerator / denominator
        print(numerator, " over ", denominator, " equals ", result )
    except ValueError:
        print("Please enter Integers only, Try Again: ")
        divide()
    except ZeroDivisionError:
        print("Number cannot be divided by 0, Try Again: ")
        divide()
    except KeyboardInterrupt:
        print("Quitter! ")
    except:
        print("I have no idea what went wrong. ")

def main():
    divide()

main()


