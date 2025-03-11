def main():
    with open(r"iterables\data\states.txt") as f:
        lines = f.read().splitlines()

    states_with_spaces = []
    
    for line in lines:
        state = line.split("\t")
        if " " in state[0]:
            states_with_spaces.append(state[0])

    for i, state_name in enumerate(states_with_spaces,1):
        print(f"{i}.{state_name}")

main()