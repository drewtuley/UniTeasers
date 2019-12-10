from itertools import permutations, combinations

# Xmas Teaser 2019
# How many words of three or more letters can be made
# from the following letters without using plurals,
# abbreviations or proper nouns.
# S, T, F, N, E, C, A, I and A
# None of the letters may be used more than once, and the last 'A' must must used
# in each word. (i.e. there may be 2 'A's and at least one).
# There is at least one nine letter word

# Note: As this code uses the 20k word list, plurals, proper nouns and abbreviations
# will have to be removed by hand...

letters = 'stfnecai'
with open('20k.txt') as words_fd:
    found_words = set()
    word_list = set(filter(lambda word: (len(word) >= 3), [x.strip() for x in words_fd]))
    for word_len in range(2, 9):
        for word1 in combinations(letters, word_len):
            new_word = list(word1)
            new_word.append('a')
            for word2 in permutations(new_word):
                word = ''.join(word2)
                if word in word_list:
                    found_words.add(word)
    for word in found_words:
        print(word)
