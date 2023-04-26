import random
import prompt


def main():
    print('Welcome to the Brain Games! ')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    n = 0
    while n < 3:
        first_num = random.randrange(1, 100)
        print(f'Question: {first_num}')
        k = 2
        answer = input('Your answer: ')
        k = 0
        for i in range(2, first_num // 2 + 1):
            if (first_num % i == 0):
                k = k + 1
        if k <= 0 and answer == 'yes':
            print("Correct!")
            n += 1
        elif k <= 0 and answer == 'no':
            print(f"'no' is wrong answer ;( .Correct answer was 'yes'."
                  f"\nLet's try again, {name}!")
            break
        elif k > 0 and answer == 'no':
            print("Correct!")
            n += 1
        elif k > 0 and answer == 'yes':
            print(f"'yes' is wrong answer ;( .Correct answer was 'no'."
                  f"\nLet's try again, {name}!")
            break
        else:
            print('no correct')

    if n == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
