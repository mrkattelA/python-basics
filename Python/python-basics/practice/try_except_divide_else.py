def divide():
    try:
        numerator = int(input("Please Enter Numerator: "))
        denominator = int(input("Please Enter Denominator: "))
        result = numerator/denominator
    except ZeroDivisionError:
        print("Numerator cannot be divided by 0, Please try again. ")
        divide()
    except ValueError:
        print("Please enter integers only, Please try again. ")
        divide()
    except KeyboardInterrupt:
        print("Quitter")
    except TypeError:
        print("Please Enter ????? only. Try Again. ")
    else:
        print(numerator, " divided by ", denominator, " is ", result)

def main():
    divide()

main()