__output = ""

def add_headers():
    c = "company" 
    r = "revenue" 
    e = "expenses" 
    p = "profit"

    _output = "{}\t{}\t{}\t{}\n".format(c,r,e,p)
    print(_output)

def add_row():
    co = input("Enter the Company name: ")
    re = int(input("Enter the revenue: "))
    ex = int(input("Enter the expenses: "))
    pr = re-ex

    co_str = co.title()
    re_str = f"{re:>,}"
    ex_str = f"{ex:>,}"
    pr_str = f"{pr:>,}"


    again = input("Again, press any key to add row or press q to Quit: ")
    if again.lower() !="q":
        add_row()
    else:
        print(__output)

    _output = "{}\t{}\t{}\t{}\n".format(co_str,re_str,ex_str,pr_str)
   # _output = "'company\n{}\t' 'Revenue\n{}\t' 'Expense\n{}\t' 'profit\n{}\n".format(co_str,re_str,ex_str,pr_str)
    print("company\t" + "Revenue\t" + "Expense\t" + "Profit\n")
    print(_output)

def main():
    add_row()
    add_headers()

main()