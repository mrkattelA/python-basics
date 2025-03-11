def main():
    total = 0
    while True:
        try:
            num = input("Please enter the number: ")
            if num.lower() == "q":
                print("The Final Total is: ", total)
                print("Good Bye")
                break
            num = int(num)
        except ValueError:
            print("Integers only. Try Again. ") 
        else:
            total += num
            print("The current total is ", total)

main()