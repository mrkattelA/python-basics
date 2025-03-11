def main():
    words =  ["woodstock", "apple", "ball", "cat", "dog",
              "egg","elephant","mango","guava","umbrella",
              "donkey", "monkey", "train"]
    three_letter_words = []

    print("Printing list with List compression and Sublist")
    three_letter_wordsss = [word for word in words if len(word) ==3]
    print(three_letter_wordsss)
    print("=====================")
    print("Normal method used.")
    for word in words:
        if len(word) == 3:
            three_letter_words.append(word)
    print(three_letter_words)

main()