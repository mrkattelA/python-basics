words = ["apple", "banana", "carrot","donuts","eggs"]

sentence = input("Please Enter your sentence: ")

for word in sentence.split():
    if word in words:
        print(f"{word} is a food. ")
        break
else:
    print("No food were in the sentence. ")