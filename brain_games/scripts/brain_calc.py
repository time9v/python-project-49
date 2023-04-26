import random
import prompt


def main():
    print('Welcome to the Brain Games! ')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')

    i = 0
    while i < 3:
        operations = ['+', '-', '*']
        random_operator = random.choice(operations)
        first_num = random.randrange(1, 10)
        second_num = random.randrange(1, 10)
        print(f'Question: {first_num} {random_operator} {second_num}')
        answer = input('Your answer: ')
        if random_operator == '+':
            result = first_num + second_num
        elif random_operator == '-':
            result = first_num - second_num
        else:
            result = first_num * second_num

        if int(answer) == result:
            print('Correct!')
            i += 1
        else:
            print(f"'{answer}' is wrong answer ;( .Correct answer was '{result}'."
                  f"\nLet's try again, {name}!")
            break
    if i == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
