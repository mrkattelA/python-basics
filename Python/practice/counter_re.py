import re
from collections import Counter

with open(r"C:\Users\mrkat\OneDrive\Desktop\Webucator\Python2\regular-expressions\Demos\Declaration_of_Independence.txt") as f:
    doi = f.read().upper()


word_list = [word for word in re.split("[^A-Z]", doi) if len(word) > 5]

c = Counter(word_list)
print(c.most_common(10))