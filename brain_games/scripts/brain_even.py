import random
import prompt


def main():
    print('Welcome to the Brain Games! ')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no"')
    i = 0
    while i < 3:
        quest = random.randrange(1, 100)
        print(f'Question: {quest}')
        answer = input('Your answer: ')
        if quest % 2 == 0 and answer == 'yes':
            print('Correct!')
            i = i + 1
        elif quest % 2 == 0 and answer != 'yes':
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'. "
                  f"\nLet's try again, {name}!")
            break

        if quest % 2 != 0 and answer == 'no':
            print('Correct!')
            i = i + 1
        elif quest % 2 != 0 and answer != 'no':
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'. "
                  f"\nLet's try again, {name}!")
            break
    if i == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
