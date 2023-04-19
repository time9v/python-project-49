import random
import math
import prompt
def main():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Find the greatest common divisor of given numbers.')
    i = 0
    while i < 3:
        first_num = random.randrange(1, 100)
        second_num = random.randrange(1, 100)
        quest = print(f'Question: {first_num} {second_num}')
        result = math.gcd(first_num, second_num)
        answer = input('Your answer: ')
        if int(answer) == result:
            print('Correct!')
            i += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'.\nLet's try again, {name}!'")
            break
    if i == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()