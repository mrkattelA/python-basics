def multiply(x, y):
    return x*y

def main():
    num1 = range(0, 10)
    num2 = range(10, 0, -1)

    multiples = []

    for i in range(len(num1)):
        multiple = multiply(num1[i],num2[i])
        multiples.append(multiple)

    for multiple in multiples:
        print(multiple)

main()