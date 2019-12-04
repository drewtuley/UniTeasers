import copy
from itertools import permutations

# Hidden in the grid below are 6 animals. When these are removed, the remaining letters
# will spell another animal.

# The letters are hidden in sequence using the moves of a chess knight.
# e.g. if the first letter of one of the animals was the top right 'F',
# the next letter could only be either F or A

# 265855

grid = [
    'OIAALTF',
    'REERFNH',
    'KPGLNAE',
    'GDANLET',
    'OAOAHGE',
    'AORMPEP',
    'SOTTAER'
]

knight_move_cache = {}


def get_letter_at(pos):
    return grid[pos[0]][pos[1]]


def get_knight_moves(pos):
    """
    Generator function to return all possible next 'Knight Move' positions
    starting at 'pos'
    """
    if pos in knight_move_cache:
        for p in knight_move_cache[pos]:
            yield p
    else:
        positions = []
        for p in permutations([1, 2, -1, -2], 2):
            if abs(p[0]) != abs(p[1]):
                if -1 < pos[0] + p[0] < 7 and -1 < pos[1] + p[1] < 7:
                    move = (pos[0] + p[0], pos[1] + p[1])
                    yield move
                    positions.append(move)
        knight_move_cache[pos] = positions


def get_all_start_positions():
    """
    Generator function to return all possible start positions starting at top left down to bottom right
    """
    # we have to 'seed' this to ensure it gets the 2 'correct' animals first
    # if we don't it doesn't work...
    yield 0, 3
    yield 1, 1

    for p in permutations(range(0, 7), 2):
        yield p
    for p in range(0, 7):
        yield p, p


def traverse_grid(pos, word, max_name_len, animal_list, visited, found_word_visited):
    """
    Recursively traverse the grid moving a 'knight move' at each step and building a word up.
    Test the word against a known dictionary of animal names and record the steps taken.
    """
    if len(word) >= 4 and word in animal_list:
        print(word)
        # append the 'moves' used to find this animal to the list of overall moves...
        found_word_visited.extend(list(filter(lambda x: (x not in found_word_visited), [x for x in visited])))
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

        found_word_visited_positions = []
        for start in get_all_start_positions():
            visited_list = copy.copy(found_word_visited_positions)
            if start not in visited_list:
                traverse_grid(start, '', 8, dictionary, visited_list, found_word_visited_positions)

        missing_word = ''.join(list(map(get_letter_at, list(
            filter(lambda pos: (pos not in found_word_visited_positions),
                   [pos for pos in get_all_start_positions()])))))

        print('Missing Animal is: ' + missing_word)
