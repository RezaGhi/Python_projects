from word import words
import random
import string

def vaild_word(words):
    word=random.choice(words)
    while ("-" or " " ) in word:
        word=random.choice(words)
    return word.upper()

def hangman():
    word=vaild_word(words)
    word_letters=set(word)
    alphabet=set(string.ascii_uppercase)
    used_letters=set()

    lives=7

    while len(word_letters) >0 and lives>0 : 
        print(f'you have {lives} lives and alreay used these letters',''.join(used_letters))

        user_letter = input('guess a letter:')
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print(f'your{user_letter} letter are not in word')
        elif user_letter in used_letters:
            print("you've used from this letter.pleas try again")
        else:
            print('you are in wrong.please try again.')
        
        
        word_li=[letter if letter in used_letters else "-" for letter in word]
        print('current word:',''.join(word_li))
    if lives==0:
        print(f'you died,the word was {word}')
    else:
        print(f'you can guess the word: {word}')
hangman()