from copy import copy
from itertools import permutations


class MathOp():

    def get_op(self):
        pass

    def calculate(self, values):
        sum = self.get_op().join(values)
        return eval(sum)


class PlusOp(MathOp):
    def get_op(self):
        return '+'


class MinusOp(MathOp):
    def get_op(self):
        return '-'


class TimesOp(MathOp):
    def get_op(self):
        return '*'


class DivideOp(MathOp):
    def get_op(self):
        return '/'


class CageClue():

    def __init__(self, cells, math_op, result, candidates):
        self.cells = cells
        self.math_op = math_op
        self.expected_result = result
        self.winning_candidates = candidates[0]
        self.candidates = set()

    def test_values(self, values):
        answer = self.math_op.calculate(values)
        return answer == self.expected_result

    def add_candidate(self, values):
        self.candidates.add(values)

    def add_candidates_to_grid(self, grid):
        for candidate in self.get_candidates():
            print(f'Add candidates {candidate}')
            cidx = 0
            for cell in self.cells:
                grid_idx = cell[0] * 6 + cell[1]
                grid[grid_idx] = candidate[cidx]
                cidx += 1
            yield grid

    def get_candidates(self):
        if len(self.candidates) > 0:
            return self.candidates
        else:
            return set([self.winning_candidates])

    def validate_candidates(self):
        return self.winning_candidates in self.candidates


def verifyClues(clues):
    grid = [0 for x in range(0, 36)]
    for clue in clues:
        for cell in clue.cells:
            idx = cell[0] * 6 + cell[1]
            grid[idx] = 1
    return len(set(grid)) == 1


def verify_grid(grid):
    for x in range(0, 6):
        r = set([grid[x * 6 + y] for y in range(0, 6)])
        c = set([grid[y * 6 + x] for y in range(0, 6)])
        if len(c) != 6 or len(r) != 6:
            return False
    return True


def progressive_verify(grid):
    for row in range(0, 6):
        sidx = row * 6
        subset = grid[sidx:sidx + 6]
        try:
            subset.index(' ')
            return True
        except ValueError:
            if len(set(subset)) != 6:
                return False
            else:
                print(row, subset)
    return True


def print_grid(g):
    for row in range(0, 6):
        sidx = row * 6
        subset = g[sidx:sidx + 6]
        print(''.join(subset))


def test_candidates_in_grid(clues, clue_idx, grid):
    if clue_idx < len(clues):
        print(f'Cage clue {clue_idx} - candidates {clues[clue_idx].candidates}')
        for g in clues[clue_idx].add_candidates_to_grid(copy(grid)):
            # print_grid(g)
            if progressive_verify(g):
                test_candidates_in_grid(clues, clue_idx + 1, g)
    else:
        # full grid
        if verify_grid(grid):
            print_grid(grid)


if __name__ == '__main__':
    clues = [
        CageClue([(0, 0), (1, 0)], DivideOp(), 2, [('3', '6')]),
        CageClue([(0, 1), (1, 1)], PlusOp(), 6, [('2', '4')]),
        CageClue([(0, 2), (1, 2), (2, 2)], PlusOp(), 10, [('4', '5', '1')]),
        CageClue([(0, 3), (0, 4)], TimesOp(), 6, [('6', '1')]),
        CageClue([(0, 5), (1, 5)], MinusOp(), 4, [('5', '1')]),
        CageClue([(1, 3), (2, 3)], MinusOp(), 1, [('3', '2')]),
        CageClue([(1, 4), (2, 4)], TimesOp(), 10, [('2', '5')]),
        CageClue([(2, 0), (2, 1)], TimesOp(), 24, [('4', '6')]),
        CageClue([(2, 5), (3, 5)], DivideOp(), 2, [('3', '6')]),
        CageClue([(3, 0), (4, 0)], DivideOp(), 2, [('2', '1')]),
        CageClue([(3, 1), (3, 2)], MinusOp(), 2, [('5', '3')]),
        CageClue([(3, 3), (3, 4)], PlusOp(), 5, [('1', '4')]),
        CageClue([(4, 1), (4, 2)], PlusOp(), 5, [('3', '2')]),
        CageClue([(4, 3), (4, 4), (5, 4)], TimesOp(), 90, [('5', '6', '3')]),
        CageClue([(4, 5), (5, 5)], DivideOp(), 2, [('4', '2')]),
        CageClue([(5, 0), (5, 1)], TimesOp(), 5, [('5', '1')]),
        CageClue([(5, 2), (5, 3)], MinusOp(), 2, [('6', '4')])
    ]
    one_to_six = [str(x) for x in range(1, 7)]

    assert verifyClues(clues)

    #for clue in clues:
        # for p in permutations(one_to_six, len(clue.cells)):
        #     if clue.test_values(p):
        #         for c in permutations(p, len(p)):
        #             clue.add_candidate(c)
        # assert clue.validate_candidates(), f'invalid candidate options {clue.candidates} for {clue.cells} - should contain {clue.winning_candidates}'

      #  print(len(clue.candidates), clue.candidates)

    grid = [' ' for x in range(0, 36)]

    test_candidates_in_grid(clues, 0, grid)
