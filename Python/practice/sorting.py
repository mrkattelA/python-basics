colors = ['red', 'blue', 'green', 'orange']

new_colors = sorted(colors)
print(new_colors)

#the reverse argument
colors.sort(reverse=True)
print(colors)

#the key arguments
colors.sort(key=len)
print(colors)

def last_name(name):
    return name.split()[-1]

people = ['George Washington', 'John Adams',
          'Thomas Jefferson', 'John Quincy Adams']

people.sort(key=last_name)
print(people)

#the key arguments with lambda function
people.sort(key = lambda name : name.split()[-1])
print(people)

#combining key and reverse
people.sort(key = len, reverse= False)
print(people)

