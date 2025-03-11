for num in range(0,6):
    print(f"{num}", end="\n")

for num in range(6):
    print(num)

for num in range(1,6,2):
    print(num)

list1 = [1,2,3,4,5]
tupple1 = (1,2,3,4,5)
dict1 = {"Math":45, "Science":55,"Social":65,"Music":75, "Art":85}

for list2 in list1:
    print(list2)
for tupple2 in tupple1:
    print(tupple2)
for dict2, dict3 in dict1.items():
    print(f"{dict2}:{dict3}")
for items in dict1.items():
    dict2 = items[0]
    dict3 = items[1]
    print(f"{dict2}:{dict3}")
