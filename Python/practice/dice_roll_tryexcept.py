dice_roll = [
    (a, b)
    for a in range(1, 7)
    for b in range(1, 7)
]

roll_counts = {}
i=0
for roll in dice_roll:
    try:
        roll_counts[sum(roll)] += 1
    except KeyError:
        roll_counts[sum(roll)] = 1

print("{")
for k, v in roll_counts.items():
        print("", k, ":", v, end="")
        i=i+1
        if i<len(roll_counts):
             print(",")
print("\n}")