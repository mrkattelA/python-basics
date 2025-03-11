def read_state(abbreviation):
    with open("iterables\data\states.txt") as st:
        states = st.read().splitlines()

    for states_row in states:
        state = states_row.split("\t")

        if state[1] == abbreviation.upper():
            return state[0]
        
    return None

def main():
    while True:
        u_i = input("Please Enter State Abbreviation or ('q' to Quit): ").upper()

        if u_i == "Q":
            print("GoodBye! ")
            break   

        state = read_state(u_i)

        if state:   
            print(f"{u_i} is the abbreviation of {state}. ")
        else:
            print(f"No State has {u_i} as an abbreviation. ")
        
main()
