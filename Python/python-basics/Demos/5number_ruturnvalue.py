def fivenumbers(num1,num2,num3=0,num4=0,num5=0):
    total = num1 + num2 + num3 + num4 + num5
    return total

def main():
    result = fivenumbers(1,2)
    print(result)
    result = fivenumbers(result,3)
    print(result)
    result = fivenumbers(result,4)
    print(result)
    result = fivenumbers(result,5)
    print(result)
    result = fivenumbers(result,6)
    print(result)