def split_list():
    food = ["spinach", "tomato", "potato", "meat", "fish"]
    vegies = food[0:3]
    non_vegies = food[3:]
    yummy = vegies + non_vegies
    print(yummy)
    print(vegies)
    print(non_vegies)

def main():
    split_list()

main()