_output = ""

def add_headers():
    # Write your code here
    pass

def add_row():
    # Write your code here

    # The rest of the function prompts the user to add another row
    # or quit. On quitting, it prints _output. Leave it as is.

    again = input("Again? Press ENTER to add a row or Q to quit. ")
    if again.lower() != "q":
        add_row()
    else:
        print(_output)

def main():
    # Call add_headers() and add_row()
    add_headers()
    add_row()

main()