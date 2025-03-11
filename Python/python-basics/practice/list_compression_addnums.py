def add_nums(num, *nums):
    total = sum(nums, num)
    nums_joined = ", ".join([str(n) for n in nums])
    print(f"The sum of {nums_joined} and {num} is {total}")
    print("===========")
    print("without using the List Compression.")
    print(f"The sum of {nums} and {num} is {total}")

def main():
    add_nums(1,2)
    add_nums(1,4,6,8)
    add_nums(1,4,2)
    add_nums(1,34,56,24,49)

main()