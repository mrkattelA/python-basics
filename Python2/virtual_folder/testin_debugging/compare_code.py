import re
import random
from timeit import repeat

def get_word():
    words = ['Charlie', 'Woodstock', 'Snoopy', 'Lucy', 'Linus',
             'Schroeder', 'Patty', 'Sally', 'Marcie']
    return random.choice(words).upper()

def green_glass_door1():
    word = get_word()
    prev_letter = ""
    for letter in word:
        letter = letter.upper()
        if letter == prev_letter:
            return True
        prev_letter = letter
    return False

def green_glass_door2():
    word = get_word()
    pattern = re.compile(r"(.)\1")
    return pattern.search(word)

td1 = repeat(green_glass_door1, number=1000, repeat=4)
td2 = repeat(green_glass_door2, number=1000, repeat=4)

print(td1,td2, sep="\n")
print("-"*70)

print("green_glass_door1 compared to green_glass_door2: ")
print(f"{sum(td1)/sum(td2):.2%}")