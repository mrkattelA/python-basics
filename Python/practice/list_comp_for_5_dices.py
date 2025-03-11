def dice_role():
    dicerolls = []
    for a in range(1, 7):
        for b in range(1, 7):
            for c in range(1, 7):
                for d in range(1, 7):
                    for e in range(1, 7):
                        roll = (a, b, c, d, e)
                        dicerolls.append(roll)
    print(f"The total number of combination is {len(dicerolls)}.")

def dice_role_nocombo():
    dicerolls = [
        (a, b, c, d, e)
        for a in range(1, 7)
        for b in range(a, 7)
        for c in range(b, 7)
        for d in range(c, 7)
        for e in range(d, 7)
    ]
    print(f"The total combination without the combos is {len(dicerolls)}")

def main():
    dice_role()
    dice_role_nocombo()

main()