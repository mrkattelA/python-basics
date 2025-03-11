colors = ['red', 'blue', 'green', 'orange']

new_colors = sorted(colors)
print(new_colors)

#the reverse argument
new_colors = sorted(colors, reverse=True)
print(new_colors)


#the key arguments
#colors.sort(key=len)
new_colors = sorted(colors, key=len)
print(new_colors)

def last_name(name):
    return name.split()[-1]

people = ['George Washington', 'John Adams',
          'Thomas Jefferson', 'John Quincy Adams']

#people.sort(key=last_name)
new_people = sorted(people, key= last_name)
print(new_people)

#the key arguments with lambda function
#people.sort(key = lambda name : name.split()[-1])
new_people = sorted(people, key= lambda name : name.split()[-1])
print(new_people)

#combining key and reverse
#people.sort(key = len, reverse= False)
new_people = sorted(people, key = len, reverse= False)
print(new_people)

