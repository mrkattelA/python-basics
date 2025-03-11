import math

def list_slicing(a):
    list_len = len(a)
    middle_len = math.ceil(list_len/2)
    list1 = a[:middle_len]
    list2 = a[middle_len:]
    print(list1,list2)

def main():
    colors = ["red", "blue", "green ", "yellow", "black"]
    list_slicing(colors)

main()