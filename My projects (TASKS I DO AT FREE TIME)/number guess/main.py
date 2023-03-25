from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TUNS = 5

def check_answer(guess, answer, turns):
    """check answer against guess. Return the numbers of turns remaining"""
    if guess > answer:
        print('To high.')
        return turns -1
    elif guess < answer:
        print('To lower')
        return turns -1
    else:
        print(f'You got it! The answer {answer}')

def set_difficulty():
    level = input('Choose a difficulty. Type "easy" or "hard": ')
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TUNS

def game():
    print(logo)
    print('Welcome to the Number Guessing Game!')
    print("I'm thinking of a number between 1 and 100")
    answer = randint(1, 101)

    turns = set_difficulty()
    guess = 0
    while guess != answer:
        print(f'You have {turns} remaining to guess the number')
        guess = int(input('Make a guess:'))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print('You`ve run out of guesses, you lose')
            return
        elif guess != answer:
            print('Guess again.')

game()
