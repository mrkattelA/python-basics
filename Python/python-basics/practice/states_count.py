def main():
    with open(r'C:\Users\mrkat\OneDrive\Desktop\Webucator\Python\iterables\data\states.txt') as st:
    #with open("iterables\data\states.txt") as st:
        states = st.read().splitlines()

    print("There are ", len(states), "states")

main()