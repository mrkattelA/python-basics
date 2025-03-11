def main():
    total = 0

    while True:
        num = input("Please Enter the number: ")

        if num == "q":
            print("Final total is ", total)
            print("Goodbye")
            break

        if not num.isdigit():
            print("Please Enter the Integers only. ")
        else: 
            total += int(num)
            print("your current total number is ", total) 
        
       

main()
        