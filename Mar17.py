import re
from itertools import permutations


# Fill in the 4x4 grid below with the following letters 'DOGDAYS'
# such that each row, column and 2x2 (corner) block has letters (in any order)
# that make common words. Each letter must only be used once.

# ..C.
# L..K
# ATE.
# .SPI

class FourLetterWords():
    words = list()

    def __init__(self):
        self.words = list()

    def append(self, word):
        if len(set([x for x in word])) == 4:
            self.words.append(word)


def get_possible_words():
    '''Construct possible 'words' by taking each permutation of DOGDAYS and inserting them into the blank space in the grid '''
    possible_words = set()
    for combo in permutations(allowed_letters, 7):
        word = matrix
        for rep in combo:
            word = re.sub(r'X', rep, word, 1)
        possible_words.add(word)
    return possible_words


def get_four_letter_words(possible_word):
    '''Get the letters for possible four letter words from each row, column and corner 2x2 block'''
    flws = FourLetterWords()

    for idx in range(0, 4):
        flws.append(possible_word[idx * 4:(idx * 4) + 4])
        w = possible_word[idx] + possible_word[idx + 4] + possible_word[idx + 8] + possible_word[idx + 12]
        flws.append(w)

    flws.append(possible_word[0:2] + possible_word[4:6])
    flws.append(possible_word[2:4] + possible_word[6:8])
    flws.append(possible_word[8:10] + possible_word[12:14])
    flws.append(possible_word[10:12] + possible_word[14:])

    return flws.words


if __name__ == '__main__':
    allowed_letters = 'dogdays'
    matrix = 'XXcXlXXkateXXspi'

    with open('20k.txt') as fd:
        dictionary = set(
            filter(lambda wd: (3 <= len(wd) < 5), [x.strip() for x in fd]))

        for possible_word in get_possible_words():
            four_letter_words = get_four_letter_words(possible_word)
            if len(four_letter_words) == 12:
                good_words = []
                for word in four_letter_words:
                    for perm_word in permutations(word, 4):
                        w = ''.join(perm_word)
                        if w in dictionary or (w[3] == 's' and w[0:3] in dictionary):
                            good_words.append(w)
                            break

                if len(good_words) == 12:
                    print(possible_word, good_words)
