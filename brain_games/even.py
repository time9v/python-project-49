import random
GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_game():
    question = random.randrange(1, 100)
    correct_answer = even_logic(question)
    return question, correct_answer


def even_logic(question):
    if question % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return answer
