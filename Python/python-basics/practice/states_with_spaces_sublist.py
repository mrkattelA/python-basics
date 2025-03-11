def main():
    with open(r"iterables\data\states.txt") as f:
        lines = f.read().splitlines()

    states = [line.split("\t")[0] for line in lines]
    states_with_spaces = [state for state in states if " " in state]
    print(states_with_spaces)

main()