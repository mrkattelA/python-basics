Company = input("Enter name of the Company: ")
Revenue = int(input("Revenue: "))
Expenses = int(input("Expenses: "))
Profit = Revenue-Expenses
Again = input("Again? Press Enter to add a row OR Press Q to Quit: ")
_output = ""

def add_row():
    Company
    Revenue
    Expenses
   
#def row():
   # print(Company \t Revenue \t Expenses \t Profit )

def add_headers():
    print("Company", " Revenue " , " Expenses " , " Profit")
    #print("is" + Company.f{:.2} + Revenue.f{:,.2f} + Expenses.f{:,.2f} + Profit.f{:,.2f})

def again():
    again = input("press y or n")
    if again.lower() != "q":
        add_row()
    else:
        print(_output)
   
def main():
    add_row()
    Again()
    if Again.lower()!= "q":
        add_row()
    else:
        print(_output)
    add_headers()
        

main