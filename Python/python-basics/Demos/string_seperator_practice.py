def insert_seperator(s="=", repeat=30):
    print(s*repeat)

def your_name(name):
    print("Hello ", name, " ! ", sep="")

def python_poem():
    print("This is the python poem \
          poem about the python ")

def good_bye(bye):
    print("Good bye, ", bye, ".", sep="")

def main():
    name = input("What is your name? ")
    insert_seperator("-",20)
    your_name(name)
    insert_seperator("-",20)
    python_poem()
    insert_seperator()
    good_bye(name)
    insert_seperator()


main()
