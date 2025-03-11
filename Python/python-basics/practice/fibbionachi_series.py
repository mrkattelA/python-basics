def fibo_series(a,b):
    a,b = 0,1
    while True:
        yield a
        a,b = b, a+b

def main():
    for i in fibo_series(0,1):
        print(i)
        if input("Press Enter for next fibbonachi series or 'q' to Quit. ") == 'q':
            print("GoodBye! ")
            break

main()