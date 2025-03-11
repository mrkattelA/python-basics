def get_state(state):
    with open(r"C:\Users\mrkat\OneDrive\Desktop\Webucator\Python\iterables\data\states.txt") as f:
        states = f.read().splitlines()

    states_line = []
    for any_states in states:
        state_sep = any_states.split("\t")[1]
        states_line.append(state_sep)
    return state in states_line

def main():
    print("Please, type as much State abberavations you know. ")
    print("Please, Seprate the States with Spaces. ")
    states = input("").split()
    #wrong_state = False
    for state in states:
        state = state.upper()
        if not get_state(state):
            print(f"{state} is not a valid state. ")
            #wrong_state = True
            break
    else:
        print(f"You got {len(states)} States")

main()
    
        