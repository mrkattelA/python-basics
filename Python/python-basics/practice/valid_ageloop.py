def valid_age(s):
    return s.isdigit() and 1 < int(s) <= 116

def main():
    age = input("how old are you? ")

    while not valid_age(age):
        age= input("Please Enter the Valid age number: ")

    age = int(age)

    if age >= 21:
        print("you can vote and drink")
    elif age >= 18:
        print("you can vote but you can't drink. ")
    else:
        print("you cannot vote or drink. ")

main()