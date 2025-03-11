_output = ""

def add_header():
    global _output

    c = "Company"
    r = "Revenue"
    e = "Expenses"
    p = "Profit"

    _output += "{:^10}\t {:^10}\t {:^10}\t {:^10}\n".format(c,r,e,p)

def add_row():
    global _output

    #print(_output)

    co = input("Enter Company: ")
    re = float(input("Enter Revenue: "))
    ex = float(input("Enter Expenses: "))
    pr = re-ex

    co_str = "{:<10}".format(co).title()
    re_str = "{:>10,.2f}".format(re)
    ex_str = "{:>10,.2f}".format(ex)
    pr_str = "{:>10,.2f}".format(pr)

    _output += "{}\t {}\t {}\t {}\n".format(co_str,re_str,ex_str,pr_str)

    again = input("Again, Press any key to add row or q to quit: ")
    if again.lower() != "q":
        add_row()
    else:
        print(_output)

def main():
    add_header()
    add_row()

main()