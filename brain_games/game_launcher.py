import prompt


def welcome_message():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def main_logic(question, correct_answer):
    print(f'Question: {question}')
    answer = prompt.string('Your answer: ')
    if answer == correct_answer:
        print('Correct!')
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")  # noqa: E501
        return False


def victory_condition(game):
    name = welcome_message()
    print(game.GAME_RULE)
    i = 0
    while i < 3:
        question, correct_answer = game.get_game()
        if main_logic(question, correct_answer):
            i += 1
        else:
            print(f"Let's try again, {name}!")
            break
    if i == 3:
        print(f'Congratulations, {name}!')
