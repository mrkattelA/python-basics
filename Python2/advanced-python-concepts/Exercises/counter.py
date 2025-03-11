from collections import Counter


with open(r"C:\Users\mrkat\OneDrive\Desktop\Webucator\Python2\advanced-python-concepts\Exercises\Declaration_of_Independence.txt") as f:
    lines = f.read()

       
words_list = [word for word in lines.upper().split() if len(word) > 5]

common_words = Counter(words_list)

print(common_words.most_common(10))
            
