def multiply(x, y):
    return x*y

def main():
    num1 = range(0, 10)
    num2 = range(10, 0, -1)

    multiples = map(multiply, num1, num2)

    for mul in multiples:
        print(mul)

main()