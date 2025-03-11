import random

def remove_random(my_list):
    x = random.choice(my_list)
    my_list.remove(x)
    return x

def main():
    colors = ["red", "yellow", "blue", "green"]
    removed_colors = remove_random(colors)
    print("The removed colors was ", removed_colors)
    print("The remaining colors are : ", colors)
    print(f"the removed colors was {removed_colors:=>10}")
    print(f"the remaining colors are {colors}")

main()