import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}'))
        if guess < random_number:
            print('Opps...Sorry, guess again. Too small.')
        elif guess > random_number:
            print('Opps...Sorry, guess again. Too big.')

    print(f'Yessir,you can have a cookie... congrats. You have guessed the number {random_number} ')


guess(100)        