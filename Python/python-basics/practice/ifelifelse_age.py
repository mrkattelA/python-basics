def main():
    age = int(input("How old are you? "))

    if  age>= 21:
        print("you can vote and drink.")
    elif age>=18:
        print("you can vote but you can't dring")
    else:
        print("you cannot vote or dring")

main()