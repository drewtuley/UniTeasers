# By changing the third letter of each of the words below, can you make another valid word.
# You have to change each word such that the third letters will reveal a ten letter word
# when read downwards.

def find_viable_options(word, dictionary):
    possibles = set()
    for l in 'abcdefghijklmnopqrstuvwxyz':
        test_word = word[0:2] + l + word[3]
        if test_word != word and test_word in dictionary:
            possibles.add(l)
    return possibles


if __name__ == '__main__':
    with open('words_alpha.txt') as fd:
        wordlist = ['bake', 'cure', 'maze', 'pest', 'neat', 'rope', 'port', 'food', 'poke', 'soda']
        # filter out a set of 10 and 4 letter words
        dictionary = set(
            filter(lambda wd: (len(wd) == 4 or len(wd) == 10), [x.strip() for x in fd]))

        # find all the viable 3rd letter options for each seed word
        word_options = list(find_viable_options(word, dictionary) for word in wordlist)

        ten_letter_words = list(filter(lambda wd: (len(wd) == 10), [wd for wd in dictionary]))
        for ten_letter_word in ten_letter_words:
            # for each ten letter word, check each letter for a match in the viable 3rd letter list
            if all(ten_letter_word[idx] in word_options[idx] for idx in range(0, 9)):
                print(ten_letter_word)
