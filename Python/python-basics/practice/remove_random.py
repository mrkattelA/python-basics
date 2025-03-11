import random

def remove_random():
    my_list = ["blue","yellow","red","orange","green"]
    random_color = my_list.remove(random.choice(my_list))
    removed_color = random_color
    print("The removed color is ",my_list.remove(random.choice(my_list)))
    print("The remaining colors are : ", my_list)

def main():
    remove_random()

main()