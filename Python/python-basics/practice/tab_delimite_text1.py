__output = ""

def create_row():
    c = input("Enter the name of Company: ")
    r = int(input("Enter the Revenue: "))
    e = int(input("Enter the expenses: "))
    p = r-e

    c_str = c.title()
    r_str = f'{r:>,}'
    e_str = f'{e:>,}'
    p_str = f'{p:>,}'

    __output = "Company \n{}\t Revenue \n{}\t Expenses \n{}\t Profit \n{}\n".format(c_str,r_str,e_str,p_str)

    again = input("Again, Press Enter to add row and q to Quit: ")
    if again.lower()!= "q":
        create_row()
    else:
        print(__output)

def create_header():
    co = "company"
    re = "revenue"
    ex = "expenses"
    pr = "Profit"

    __output = " Company + {}\t Revenue + {}\t Expenses + {}\t Profit + {}\n"

def main():
    create_header()
    create_row()

main()