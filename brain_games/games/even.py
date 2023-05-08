import random

GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(question):
    return question % 2 == 0


def get_game():
    question = random.randrange(1, 100)
    correct_answer = 'yes' if is_even(question) else 'no'
    return question, correct_answer
