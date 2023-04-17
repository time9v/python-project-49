import random
import prompt


def main():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no"')
    i = 0
    while i < 3:
        quest = random.randrange(1, 100)
        a = print(f'Question: {quest}')
        b = input('Your answer: ')
        if quest % 2 == 0 and b == 'yes':
            print('Correct!')
            i = i + 1
        elif quest % 2 == 0 and b != 'yes':
            print(f"'{b}' is wrong answer ;(. Correct answer was 'yes'. Let's try again, {name}!")
            break

        if quest % 2 != 0 and b == 'no':
            print('Correct!')
            i = i + 1
        elif quest % 2 != 0 and b != 'no':
            print(f"'{b}' is wrong answer ;(. Correct answer was 'no'. Let's try again, {name}!")
            break
    if i == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
