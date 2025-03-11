def your_name():
    your_names = input("what is your name? ")
    print ("Hello, ", your_names, "!", "How can I help you with? ", sep="")
    your_names

def line_seperator():
    print("=====")
    

def recite_poem():
    print("How about the python poem!")
    line_seperator()
   # your_names from def your_name()
    line_seperator()
    print("This is a poem about the python")
    print("python is a programing language")
    print("it is very useful programming language")
    print("with python you can write program")

def say_goodbye():
    print(your_name, "Good Bye", sep="")

def main():
    your_name()
    line_seperator()
    recite_poem()
    line_seperator()
    say_goodbye()
    line_seperator()

main()
line_seperator()