num = int(input("Enter the number"))

for i in range(5):
    if i == num:
      break
    print(i)
else:
   print("you exceed the number", num)

#Example 2

i = 0
num = int(input("Enter the number: "))

while i <= 5:
   if i == num:
      break
   print(i)
   i += 1
else:
   print("you exceed the number:")
   
