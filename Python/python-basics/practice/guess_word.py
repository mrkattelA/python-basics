import random

def get_word():

    words = ['Charlie', 'Woodstock', 'Snoopy', 'Lucy', 'Linus',
             'Schroeder', 'Patty', 'Sally', 'Marcie']
    return random.choice(words).upper()

def main():
    x = get_word()
    print(f"The words contain {len(x)} letters.")
    
    y = input(f"Guess a letter or {len(x)} letter word.: ").upper()

    z = list(x)

    #print(z)

    while not y in z:
        print(f"Sorry, the word has no '{y}'. ")
        print(end = "*" *len(x))

        y = input(f"Guess a letter or {len(x)} letter word.: ").upper()

        if y in list(x):
            print(x)

main()