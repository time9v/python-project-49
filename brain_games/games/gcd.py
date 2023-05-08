import math
import random

GAME_RULE = 'Find the greatest common divisor of given numbers.'


def get_game():
    first_num = random.randrange(1, 100)
    second_num = random.randrange(1, 100)
    question = f'{first_num} {second_num}'
    correct_answer = str(math.gcd(first_num, second_num))
    return question, correct_answer
