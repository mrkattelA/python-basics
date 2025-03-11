__output = ""

def add_header():
    c = "Company"
    r = "Revenue"
    e = "Expenses"
    p = "Profit"

    __output = "{}\t {}\t {}\t {}\n".format(c,r,e,p)
    __output += __output 
    #print(__output)

def add_row():
    c= input("Enter name of the company: ")
    r= int(input("Enter the Revenue: "))
    e= int(input("Enter the expenses: "))
    p= r-e

    c_str = c.title()
    r_str = f"{r:>,}"
    e_str = f"{e:>,}"
    p_str = f"{p:>,}"

    again = input("Again, Press Any key to Continue or q to Quit :")
    if again!= "q":
        add_row()
    else:
        print(__output)

    #_output = "c_str\n{}\t r_str\n{}\t e_str\n{}\t p_str\n{}\n".format(c_str,r_str,e_str,p_str)
        
    __output = "{}\t {}\t {}\t {}\n".format(c_str,r_str,e_str,p_str)
    __output += __output 

    #print("Company\t Revenue\t Expenses \t Profit\n", _output)
    print(__output)

def main():
    add_header()
    add_row()

main()