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
        spisok_quests = []
        for x in range(quest, quest2, 2):
            spisok_quests.append(x)
        random_choice = random.choice(spisok_quests)

        if random_choice in spisok_quests:
            secret = '..'
            spisok_quests = [index if index != random_choice else secret for index in spisok_quests]

        new = " ".join(map(str, spisok_quests))
        print(f'Qustion: {new}')
        answer = input('Your answer: ')
        if int(answer) == random_choice:
            print('Correct!')
            i += 1
        elif int(answer) != random_choice:
            print(f"'{answer} is wrong answer ;(. Correct answer was {random_choice}."
                  f"\nLet's try again, {name}!")
            break
    if i == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()

