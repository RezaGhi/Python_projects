import random
def computer_guess():
    print('please choose a number between 1 and 100 and remember that\n.')
    print('if pc\'s choice is higher enter h ,if pc\'s choice is lower enter l ,if it is equal enter e.\n')
    min=1
    max=100
    while True:
        c_guess=random.randint(min,max)
        your_help=input(f'the computer\'s guess is {c_guess},is it higher,lower or equal?')
        if your_help.lower()=='h':
            max=c_guess-1
        elif your_help.lower()=='l':
            min=c_guess+1
        elif your_help.lower()=='e':
            print('you won.')
            break
        else:
            print('you are in wrong')
            break            

computer_guess()
