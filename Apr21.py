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
        dictionary = set(
            filter(lambda wd: (len(wd) == 4 or len(wd) == 10), [x.strip() for x in fd]))

        word_options = list()
        for word in wordlist:
            options = find_viable_options(word, dictionary)
            word_options.append(options)

        ten_letters = list(filter(lambda wd: (len(wd) == 10), [wd for wd in dictionary]))
        for ten_letter in ten_letters:
            match = True
            for idx in range(0, 9):
                if ten_letter[idx] not in word_options[idx]:
                    match = False
                    break
            if match:
                print(ten_letter)
