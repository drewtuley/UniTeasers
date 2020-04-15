# Hidden words

# Hidden in the 'grid' are eight, 7 letter words.
# Each word begins with the central 'p' and you can move one letter in any direction
# to the next letter.
# All of the letters are used exactly once each (apart from the 'P' of course)

# What are the words?

from copy import copy
from itertools import combinations


def cyclic_grid(pos):
    for dx, dy in [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]:
        if -1 < (pos[0] + dx) < 7 and -1 < (pos[1] + dy) < 7:
            yield pos[0] + dx, pos[1] + dy


def get_word_from_path(matrix, path):
    return ''.join([matrix[pos[1]][pos[0]] for pos in path])


if __name__ == '__main__':
    grid = [
        'disisak',
        'mrcncye',
        'acyahna',
        'hyspibl',
        'ierolls',
        'cmpurat',
        'muilaer'
    ]
    with open('20k.txt') as fd:
        # create a dictionary from our word list filtering on words that start with 'p' and have a valid 2nd letter
        # (i.e. those letters that are next to the 'p' in the grid)
        dictionary = set(
            filter(lambda wd: (len(wd) == 7 and wd[0] == 'p' and wd[1] in 'yrsoliha'), [x.strip() for x in fd]))

        # starting at the 'P' in the center (3,3), generate a list of distinct paths of 7 steps each
        # making sure we don't double back on ourselves or go outside the bounds of the grid
        start = (3, 3)
        candidates = list()
        fixed_second_points = list()
        for next_col, next_row in cyclic_grid(start):
            fixed_second_points.append((next_col, next_row))
        for second_points in fixed_second_points:
            path = list([start])
            path.append(second_points)
            for third in cyclic_grid(second_points):
                p3 = copy(path)
                if third not in p3:
                    p3.append(third)
                    for fourth in cyclic_grid(third):
                        p4 = copy(p3)
                        if fourth not in p4:
                            p4.append(fourth)
                            for fifth in cyclic_grid(fourth):
                                p5 = copy(p4)
                                if fifth not in p5:
                                    p5.append(fifth)
                                    for sixth in cyclic_grid(fifth):
                                        p6 = copy(p5)
                                        if sixth not in p6:
                                            p6.append(sixth)
                                            for seventh in cyclic_grid(sixth):
                                                p7 = copy(p6)
                                                if seventh not in p7:
                                                    p7.append(seventh)
                                                    # at this point we have a 7 step path, so
                                                    # find the word that it makes
                                                    word = get_word_from_path(grid, p7)
                                                    if word in dictionary:
                                                        # if the word is in the dictionary add the path
                                                        # to the list of candidates IGNORING THE 'P' at position 0
                                                        candidates.append(p7[1:])

        # generate combinations of 8 choices from the candidate paths
        for candidate_set in combinations(candidates, 8):
            good_set = True
            # create a working set from the 1st candidate
            working_set = set(candidate_set[0])
            for check_set in candidate_set[1:]:
                if any(item in working_set for item in check_set):
                    good_set = False
                    break
                else:
                    # if none of the positions in each subsequent set aren't in the working set
                    # add them to it
                    working_set.update(check_set)
            if good_set:
                # we have a 'good set' - i.e. a set of paths that don't conflict
                # so find the words they make
                for cs in candidate_set:
                    word = get_word_from_path(grid, cs)
                    print('p' + word)
