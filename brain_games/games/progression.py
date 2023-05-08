import random

GAME_RULE = 'What number is missing in the progression?'


def generate_progression():
    first_num = random.randrange(1, 50)
    last_num = first_num + 20
    progression = []
    for x in range(first_num, last_num, 2):
        progression.append(x)
    return progression


def get_game():
    progression = generate_progression()
    correct_answer = random.choice(progression)
    if correct_answer in progression:
        secret = '..'
        progression = [index if index != correct_answer else secret for index in progression]  # noqa: E501
    question = " ".join(map(str, progression))
    correct_answer = str(correct_answer)
    return question, correct_answer
