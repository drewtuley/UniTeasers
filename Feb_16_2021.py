# On each row place a four letter word that goes after the word to the left and before the word to the right
# (i.e. SECOND — HAND — SHAKE).
# When completed the third letters of the added words will give another word reading downwards.
# What is it?
# WITH STRING
# OUT EFFECT
# PUPPY HEART
# DUTY HOLD
# BACK SOME
# BUBBLE MAT
from copy import copy


def find_possible_seven_letter_words(list_of_four_letter_words, index, output):
    if index < len(list_of_four_letter_words):
        copy_output = copy(output)
        next_index = index+1
        for four_letter_word in list_of_four_letter_words[index]:
            working_str = copy_output + four_letter_word[2]
            yield from find_possible_seven_letter_words(list_of_four_letter_words, next_index, working_str)
    else:
        yield output


if __name__ == '__main__':
    word_pairs = [
        ('WITH', 'STRING'),
        ('OUT', 'EFFECT'),
        ('PUPPY', 'HEART'),
        ('DUTY', 'HOLD'),
        ('BACK', 'SOME'),
        ('BUBBLE', 'MAT')
    ]
    with open('words_alpha.txt') as fd:
        dictionary = set(filter(lambda wd: (len(wd) >= 4), [rl.strip().upper() for rl in fd]))

        four_letter_words = set(filter(lambda wd: (len(wd) == 4), [wd for wd in dictionary]))
        lh_dictionary = set()
        rh_dictionary = set()

        for wd in dictionary:
            for pair in word_pairs:
                if wd.startswith(pair[0]):
                    lh_dictionary.add(wd)
                elif wd.endswith(pair[1]):
                    rh_dictionary.add(wd)

        fours = []
        for pair in word_pairs:
            this_four = set()
            for four in four_letter_words:
                left = pair[0] + four
                right = four + pair[1]
                if left in lh_dictionary and right in rh_dictionary:
                    print(f'* {pair[0]} {four} {pair[1]}')
                    this_four.add(four)
            fours.append(this_four)

        #print(fours)

        possibilities = set()
        for possibility in find_possible_seven_letter_words(fours, 0, ''):
            if possibility in dictionary and possibility not in possibilities:
                print(possibility)
                possibilities.add(possibility)
