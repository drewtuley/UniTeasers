# hidden animals
from itertools import permutations
import copy

grid = [
    'OIAALTF',
    'REERFNH',
    'KPGLNAE',
    'GDANLET',
    'OAOAHGE',
    'AORMPEP',
    'SOTTAER'
]


def get_letter_at(pos):
    return grid[pos[0]][pos[1]]


def get_knight_moves(pos):
    for p in permutations([1, 2, -1, -2], 2):
        if abs(p[0]) != abs(p[1]):
            if -1 < pos[0] + p[0] < 7 and -1 < pos[1] + p[1] < 7:
                yield pos[0] + p[0], pos[1] + p[1]


def get_all_positions():
    yield 0, 3
    yield 1, 1

    for p in permutations(range(0, 7), 2):
        yield p
    for p in range(0, 7):
        yield p, p


def traverse_grid(pos, word, max_name_len, animal_list, visited, found_word_visited):
    if word in animal_list and len(word) >= 4:
        print(word)
        for p in visited:
            if p not in found_word_visited:
                found_word_visited.append(p)
        # need to back out here completely
        return True
    elif len(word) > max_name_len:
        return

    if pos not in visited:
        word += get_letter_at(pos)
        visited.append(pos)
        for move in get_knight_moves(pos):
            if traverse_grid(move, word, max_name_len, animal_list, copy.copy(visited), found_word_visited):
                return True


if __name__ == '__main__':
    with open('animals.txt') as fd:
        dictionary = set(filter(lambda word: (' ' not in word), [x.strip().upper() for x in fd]))
        longname = len(max(dictionary, key=lambda x: len(x)))
        found_word_visited_positions = []
        for start in get_all_positions():
            visited_list = copy.copy(found_word_visited_positions)
            if start not in visited_list:
                traverse_grid(start, '', 8, dictionary, visited_list, found_word_visited_positions)

        missing_word = ''
        for pos in get_all_positions():
            if pos not in found_word_visited_positions:
                missing_word += get_letter_at(pos)
        print('Missing Animal is: '+missing_word)
