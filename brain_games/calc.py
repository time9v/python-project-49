import random
GAME_RULE = 'What is the result of the expression?'


def get_game():
    random_operator = random.choice(['+', '-', '*'])
    first_num = random.randrange(1, 10)
    second_num = random.randrange(1, 10)
    question = f'{first_num} {random_operator} {second_num}'
    correct_answer = calculate_expression(question)
    return question, correct_answer


def calculate_expression(question):
    answer = str(eval(question))
    return answer





