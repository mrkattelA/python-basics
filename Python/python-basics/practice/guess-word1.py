import random

def get_words():
    words = ["apple", "ball", "cat", "dog",
             "elephant", "frog", "ground",
             "horse","inkjets"]
    
    return random.choice(words).upper()

def check(word,guesses):
    status = ""
    last_guess = guesses[-1]
    matches = 0

    for letter in word:
        status += letter if letter in guesses else "*"

        if letter == last_guess:
            matches += 1

    if matches > 1:
        print(f" the word has {matches} '{last_guess}'s. ")
    elif matches == 1:
        print(f"the word has {last_guess}. ")
    else:
        print(f"Sorry, there is no word {last_guess}. ")

    return status

def main():
    word = get_words()
    n = len(word)
    guesses = []
    guessed = False
    print(f"the word contains {n} letters. ")

    while not guessed:
        guess = input(f'guess the {n} letter word: ')
        guess = guess.upper()
        if guess in guesses:
            print(f'you already have guessed {guess}. ')
        elif len(guess) == n:
            guesses.append(guess)
            if guess == word:
                guessed = True
            else:
                print("sorry that is incorrect. ")
        elif len(guess) == 1:
            guesses.append(guess)
            result = check(word,guesses)
            if result == word:
                guessed = True
            else:
                print(result)
        else:
            print("Invalid Entry")

    print(f"{word} it is, it took {len(guesses)} tries. ")

main()