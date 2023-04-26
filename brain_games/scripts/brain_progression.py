import random
import prompt


def main():
    print('Welcome to the Brain Games! ')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What number is missing in the progression?')
    i = 0
    while i < 3:
        quest = random.randrange(1, 50)
        quest2 = quest + 20
        quests = []
        for x in range(quest, quest2, 2):
            quests.append(x)
        rchoise = random.choice(quests)

        if rchoise in quests:
            secret = '..'
            quests = [index if index != rchoise else secret for index in quests]

        new = " ".join(map(str, quests))
        print(f'Question: {new}')
        answer = input('Your answer: ')
        if int(answer) == rchoise:
            print('Correct!')
            i += 1
        elif int(answer) != rchoise:
            print(f"'{answer} is wrong answer ;(. Correct answer was {rchoise}."
                  f"\nLet's try again, {name}!")
            break
    if i == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
