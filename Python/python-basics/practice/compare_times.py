import time
import random

iterations = int(input("Number of iterations: "))

#Concatinating String
start_time = time.perf_counter()
numbers = ""
for i in range(iterations):
    num = random.randint(1,100)
    numbers += "," + str(num)
end_time = time.perf_counter()
td1 = end_time - start_time
print("From String Concatination: ", td1)

#Appending to the List
start_time = time.perf_counter()
numbers = []
for i in range(iterations):
    num = random.randint(1,100)
    numbers.append(str(num))
numbers = ", ".join(numbers)
end_time = time.perf_counter()
td2 = end_time - start_time
print("From List: ", td2)

#List Compression Method
start_time = time.perf_counter()
numbers = [str(random.randint(1,100)) for num in range(iterations)]
numbers = ", ".join(numbers)
end_time = time.perf_counter()
td3 = end_time-start_time
print("From List Compression: ", td3)

print(f"""Total Number of iterations for{iterations}:
String Concatination: {td1}
List                : {td2}
List Compression    : {td3}
The String Concatination is {round(td1/td3,2)} times slower than List Compression.\n""")
