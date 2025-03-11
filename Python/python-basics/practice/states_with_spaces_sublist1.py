def main():
    with open(r"iterables\data\states.txt") as f:
        lines = f.read().splitlines()

    states_with_spaces = [state.split("\t")[0]
                        for state in lines
                        if " " in state]
    print(states_with_spaces)

main()