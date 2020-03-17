from itertools import permutations
import re


# Fill in the 4x4 grid with the following letters 'DOGDAYS'
# such that each row, column and 2x2 block has letters in any order
# that make common words.

# ..C.
# L..K
# ATE.
# .SPI

def get_possible_words():
    possible_words = set()
    for combo in permutations(allowed_letters, 7):
        word = matrix
        for rep in combo:
            word = re.sub(r'X', rep, word, 1)
        possible_words.add(word)
    return possible_words


def get_four_letter_words(possible_word):
    four_letter_words = []

    four_letter_words.append(possible_word[0:4])
    four_letter_words.append(possible_word[4:8])
    four_letter_words.append(possible_word[8:12])
    four_letter_words.append(possible_word[12:])
    for idx in range(0, 4):
        w = possible_word[idx] + possible_word[idx + 4] + possible_word[idx + 8] + possible_word[idx + 12]
        four_letter_words.append(w)

    four_letter_words.append(possible_word[0:2] + possible_word[4:6])
    four_letter_words.append(possible_word[2:4] + possible_word[6:8])
    four_letter_words.append(possible_word[8:10] + possible_word[12:14])
    four_letter_words.append(possible_word[10:12] + possible_word[14:])

    for word in four_letter_words:
        letters = set()
        for letter in word:
            letters.add(letter)
        if len(letters) != 4:
            return []

    return four_letter_words

if __name__ == '__main__':
    allowed_letters = 'dogdays'
    matrix = 'XXcXlXXkateXXspi'

    with open('20k.txt') as fd:
        dictionary = set(
            filter(lambda wd: (len(wd) >= 3 and len(wd)< 5), [x.strip() for x in fd]))

    possible_words = get_possible_words()
    for possible_word in possible_words:
        four_letter_words = get_four_letter_words(possible_word)

        good_words = []
        for word in four_letter_words:
            for perm_word in permutations(word, 4):
                w = ''.join(perm_word)
                if w in dictionary:
                    good_words.append(w)
                    break
                if w[3] == 's' and w[0:3] in dictionary:
                    good_words.append(w)
                    break

        if len(good_words) == 12:
            print(possible_word, good_words)
