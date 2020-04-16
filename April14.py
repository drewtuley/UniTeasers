# Bowling Game
# At a recent bowling match, two games were played:
# * Kelly beat Sam in both games, also Reed beat Jamie in both games [RULE1]
# * The winner in game 1 came second in game 2                       [RULE2]
# * Reed won game 2 and Jamie beat Sam in game 1                     [RULE3]
# * No player got the same placing twice                             [RULE4]
# Can you determine who finished where in each game ?

from itertools import permutations


def rule1(game1, game2):
    return game1.index('K') < game1.index('S') and game2.index('K') < game2.index('S') and game1.index(
        'R') < game1.index('J') and game2.index('R') < game2.index('J')


def rule2(game1, game2):
    return game1[0] == game2[1]


def rule3(game1, game2):
    return game2[0] == 'R' and game1.index('J') < game1.index('S')


def rule4(game1, game2):
    return not any(game1.index(p) == game2.index(p) for p in 'KSJR')


if __name__ == '__main__':
    game_results = [game for game in permutations('KSJR', 4)]

    for game1, game2 in permutations(game_results, 2):
        if all(func(game1, game2) for func in [rule1, rule2, rule3, rule4]):
            print(game1, game2)
