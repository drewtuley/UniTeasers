# How many squares, of any size, can you find on a chess board which do not contain a Rook?
# The 'rooks' in question being on squares (0,7),(3,4),(5,5) and (6,2)
from typing import List, Tuple

rooks: List[Tuple[int, int]] = [(7, 0), (4, 3), (5, 5), (2, 6)]


def square_contains_rook(square):
    return len(set(filter(
        lambda rook: (rook[0] >= square[0] and rook[0] < square[2] and rook[1] >= square[1] and rook[1] < square[3]),
        [r for r in rooks]))) > 0


def cell_in_square(col, row, square):
    return col >= square[0] and col < square[2] and row >= square[1] and row < square[3]


def cell_is_rook(col, row):
    return (col, row) in rooks


def dump_square(square):
    for start_row in range(0, 8):
        row = ''
        for start_col in range(0, 8):
            if cell_in_square(start_col, start_row, square):
                row += 'X'
            elif cell_is_rook(start_col, start_row):
                row += 'R'
            else:
                row += '.'
        print(row)


if __name__ == '__main__':
    none_rook_count = 0
    square_count = {1:set(), 2:set(), 3:set(), 4:set()}
    for start_row in range(0, 8):
        for start_col in range(0, 8):
            for size in range(1, 9 - max(start_row, start_col)):
                # print(start_row, start_col, size)
                square = (start_col, start_row, start_col + size, start_row + size)
                # print(square)
                if not square_contains_rook(square):
                    square_count[size].add(square)
                    none_rook_count += 1
                    if size == 3:
                        print(square)
                        dump_square(square)
    print(none_rook_count)
    print(square_count[3])
