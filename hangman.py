from words import words
import random
import string

def get_valid_word(words):
    word = random.choice(words).upper()
    while('-' in word or " " in word):
        word = random.choice(words).upper()

    return word

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #letters in the word that already guessed
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  #what the user has guessed

    lives = 6

    #getting user input
    while len(word_letters)>0 and lives>0:
        #letters used
        print("you have", lives, "lives left and you have used these letters: "," ".join(used_letters))

        #what current word is
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("current word is : "," ".join(word_list))

        user_letters = input("guess a letter: ").upper()
        if user_letters in alphabet - used_letters:
            used_letters.add(user_letters)
            if user_letters in word_letters:
                word_letters.remove(user_letters)

            else:
                lives = lives-1 #take away a life if wrong
                print("letter is not in the word.")

        elif user_letters in used_letters:
            print("you have already guessed that character, try again!")
        else:
            print("invalid character, try again bro!!")

    #gets here when len(word_letters)==0 or when lives==0
    if lives==0:
        print("You died, sorry the word was ", word)
    else:
        print("you guessed the word ", word, "!!")

    print()

hangman()
