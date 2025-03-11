i = 1
items = ["apple ", "ball ","cat ", "dog ","egg " ]
for item in items:
    print(i, item, sep = ". ")
    i +=1

print("")
print("Next line:\n")

for i, all_item in enumerate(items,1):
    print(i, all_item, sep = "> ")