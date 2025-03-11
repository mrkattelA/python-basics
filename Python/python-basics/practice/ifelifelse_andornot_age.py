def main():
    age = int(input("How old are you? :"))
    citizen = input("Are you citizen, press y to say yes :" ).lower() == "y"

    if  age>= 21 and citizen:
        print("you can vote and drink.")
    elif age>=21:
        print("you cannot vote but you can drink")
    elif age>=18 and citizen:
        print("you can vote but you can't drink")
    else:
        print("you cannot vote or drink")

main()