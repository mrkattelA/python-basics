def is_odd(num):
    return num % 2

def main():
    nums = range(0,10)

    odd_num = filter(is_odd, nums)

    for num in odd_num:
        print(num)

main()