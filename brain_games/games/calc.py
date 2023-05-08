import random

GAME_RULE = 'What is the result of the expression?'


def calculate_expression(first_num, random_operator, second_num):
    if random_operator == '+':
        answer = first_num + second_num
    elif random_operator == '-':
        answer = first_num - second_num
    else:
        answer = first_num * second_num
    return answer


def get_game():
    random_operator = random.choice(['+', '-', '*'])
    first_num = random.randrange(1, 10)
    second_num = random.randrange(1, 10)
    question = f'{first_num} {random_operator} {second_num}'
    correct_answer = calculate_expression(first_num, random_operator, second_num)
    return question, str(correct_answer)

print(get_game())