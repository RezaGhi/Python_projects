'''
import random as rnd
computer_guess=rnd.randint(1,10)
print('you have 3 turns to guees the number that I choose.\nGOOD LOCK:)\n')
for i in range(3):
    your_guess=int(input('commom!!! guess a number:'))
    if computer_guess>your_guess:
        print('you must enter higher number!!!')
    elif computer_guess<your_guess:
        print('you must enter lower number!!!')
    elif computer_guess==your_guess:
        print('congratulationnnnnnnnn\nyou woooooooooon:):):)')
        break
    else:
        print('you are in wrong!')'''

import random
def game(num):
    c_num=random.randint(1,num)
    guess=0
    while guess != c_num:
        guess = int(input(f'please enter a number between 1 and {num}: '))
        if guess>c_num:
            print('choose lower one.')
        elif guess<c_num:
            print('choose higher one')
    print(f'you won. our number is {c_num}')

game(10)
            