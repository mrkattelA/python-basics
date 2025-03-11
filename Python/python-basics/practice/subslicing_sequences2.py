import math

def list_slicing(org_list):
    list_len = len(org_list)
    mid_round_len = math.ceil(list_len/2)
    list1 = org_list[:mid_round_len]
    list2 = org_list[mid_round_len:]
    return [list1, list2]

def main():
    fruits = ["apple", "banana", "carrot", "dragon fruit", "etc"]
    fruits_slicing = list_slicing(fruits)
    print(fruits_slicing)
    print(fruits_slicing[0])
    print(fruits_slicing[1])

main()