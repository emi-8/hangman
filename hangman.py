import random
import string
from words import words


def get_valid_word(words):
    word = random.choice(words)
    while ' ' in words or ',' in words:
        word = random.choice(words)

    return word.upper()



def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters used in the target word
    alphabet = set(string.ascii_uppercase) 
    used_letters = set() # letters player already used

    life = 10

    while len(word_letters) > 0 and life > 0:
        print('You have', life, 'lives left and you used these letters: ', ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters: 
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter) # take away the correct letter from the letters list
            else:
                life -= 1
                print('Letter is not in the word')

        elif user_letter in used_letters:
            print('You already guessed the letter. Please try again!')
        else:
            print('Invalid character. Please try again!')
    if life == 0:
        print('You died!! The correct word is', word)
    else:
        print('You win! You guessed the correct word', word)

hangman()