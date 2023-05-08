import random

GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(question):
    k = 0
    for i in range(2, question // 2 + 1):
        if question % i == 0:
            k += 1
    if k <= 0:
        return True
    else:
        return False


def get_game():
    num = random.randrange(1, 100)
    question = num
    correct_answer = 'yes' if is_prime(question) else 'no'
    return question, correct_answer
