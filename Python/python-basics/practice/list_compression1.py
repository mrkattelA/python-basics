def initials(name):
    fullname = name.split(" ")
    inits = (fullname[0][0], fullname[1][0])
    return inits

def main():
    names = ["Graham Chapman ", "John Cleese ", "Eric Idle", 
            "Terry Gillam ", "Terry Jones", "Michael Palin"]
    
    print("==============================")
    print("This is normal list comprehension.")
    initsFor = []
    for name in names:
        initsFor.append(initials(name))
    for na in initsFor:
        print(f"{na[0]}.{na[1]}")

    print("================================")
    print("This is sublist example")
    inits = [initials(name) for name in names]
    for i in inits:
        print(f'{i[0]}.{i[1]}.')

main()