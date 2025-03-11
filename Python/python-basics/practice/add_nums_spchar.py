def add_number(num,*nums):
    total = sum(nums,num)
    print(f"the sum of {nums} and {num} is {total}")

def main():
    add_number(2,3)
    add_number(2,4,6)
    add_number(2,5,7,8)
    add_number(5,6,7,8,9)
    add_number(4,6,7,8,9,2)
    add_number(1,2,3,4,5,6,7,8)
    add_number(1,2,3,4,5,6,7,8,9)
    add_number(1,2,3,4,5,6,7,8,9,0.5)
    add_number(1,2,3,4,5,6,7,8,9,0,-1)

main()