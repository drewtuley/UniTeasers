from itertools import permutations

# Using the letters AAEENNPPPPSS complete the grid below. The grid reads the same across as down.

# S...
# .A..
# ..E.
# ...T


dictionary = []


def test_words_against_dictionary(words, valid_words):
    invalid_words = []
    print('Test words: ' + ','.join(words))
    for word_to_test in words:
        if word_to_test not in valid_words:
            if word_to_test not in dictionary:
                invalid_words.append(word_to_test)
            else:
                valid_words.append(word_to_test)

    return invalid_words


if __name__ == '__main__':
    with open('20k.txt') as fd:
        for raw_l in fd:
            l = raw_l.strip()
            if len(l) == 4:
                dictionary.append(l)

    test = test_words_against_dictionary(['snap', 'nape', 'apes', 'pest'], [])
    if len(test) == 0:
        print('test passes OK')
    else:
        print('Fail: Those words should pass OK')
        exit(1)

    invalid_word_cache = []
    valid_word_cache = []
    # as the grid is a diagonally symmetric we only need half the letters
    for p in permutations(['a', 'e', 'n', 'p', 'p', 's']):
        # form the 4 words using the following indices into 'p'
        # S012
        # 0A34
        # 13E5
        # 245T
        words_to_test = [
            's' + p[0] + p[1] + p[2],
            p[0] + 'a' + p[3] + p[4],
            p[1] + p[3] + 'e' + p[5],
            p[2] + p[4] + p[5] + 't'
        ]

        if not any(word in invalid_word_cache for word in words_to_test):
            bad_words = test_words_against_dictionary(words_to_test, valid_word_cache)
            if len(bad_words) == 0:
                print(words_to_test)
                break
            else:
                invalid_word_cache.extend(bad_words)
