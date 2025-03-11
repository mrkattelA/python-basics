import random

def remove_color(my_list):
    x = my_list.remove(random.choice(my_list))
    return x

def main():
    colors = ["red", "yellow", "green", "blue"]
    removed_colors = remove_color(colors)
    print("the color removed is : ", removed_colors)
    print(colors)
    print(f"the list of colors is {colors}")

main()