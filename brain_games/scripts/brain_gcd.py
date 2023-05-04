#!/usr/bin/env python3


from brain_games import gcd
from brain_games.game_launcher import victory_condition


def main():
    victory_condition(gcd)


if __name__ == '__main__':
    main()
