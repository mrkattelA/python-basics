def main():
    dice_roll = []
    for a in range(1, 7):
        for b in range(1, 7):
            roll = (a, b)
            dice_roll.append(roll)

    print(dice_roll)

main()