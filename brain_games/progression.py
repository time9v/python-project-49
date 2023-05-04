import random
GAME_RULE = 'What number is missing in the progression?'


def get_game():
    quest = random.randrange(1, 50)
    quest2 = quest + 20
    quests = []
    for x in range(quest, quest2, 2):
        quests.append(x)
    correct_answer = random.choice(quests)
    if correct_answer in quests:
        secret = '..'
        quests = [index if index != correct_answer else secret for index in quests] # noqa: E501

    question = " ".join(map(str, quests))
    correct_answer = str(correct_answer)
    return question, correct_answer
