def get_states(state):
    with open(r"C:\Users\mrkat\OneDrive\Desktop\Webucator\Python\iterables\data\states.txt") as f:
        states = f.read().splitlines()
        
    states_avv = []
    for state_row in states:
        states_avvs = state_row.split('\t')[1]
        states_avv.append(states_avvs)

    return state in states_avv

def main():
    print("Name as many abbreviations that you know. ")
    print("Seperate with them spaces. ")
    states = input(" ").split()
    wrong_state = False
    for state in states:
        state = state.upper()
        if not get_states(state):
            print(f"{state} is not the valid state. ")
            wrong_state = True
            break

    if not wrong_state:
        print(f"you named {len(states)} states.")
    

main()
