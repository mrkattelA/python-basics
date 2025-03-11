#boys = open("python-basics/data/1880-boys.txt")
#content1 = boys.read()
#print(content1)
#boys.close()
#girls = open("python-basics/data/1880-girls.txt")
#content2 = girls.read()
#print(content2)
#girls.close()

#with open("python-basics/data/1880-all.txt", "w") as all:
#    all.write(content1 + '\n' + content2)

with open("python-basics/data/1880.txt") as boys:
    boys.read()
    print(boys)
with open("python-basics/data/1880-girls.txt") as girls:
    girls.read()
    print(girls)