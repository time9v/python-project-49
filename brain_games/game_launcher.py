import prompt
from brain_games.cli import welcome_user


def start_game(game):
    name = welcome_user()
    print(game.GAME_RULE)
    rounds = 0
    while rounds < 3:
        question, correct_answer = game.get_game()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')

        if answer == correct_answer:
            print('Correct!')
            rounds += 1

        else:
            print(f'\'{answer}\' is wrong answer ;(. '
                  f'Correct answer was \'{correct_answer}\'.'
                  f"\nLet's try again, {name}!")
            return

    print(f'Congratulations, {name}!')
