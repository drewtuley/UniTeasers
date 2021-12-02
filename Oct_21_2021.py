from itertools import combinations

if __name__ == '__main__':
    base_words = {'stamp': [], 'curry': [], 'aches': [], 'snack': [], 'broom': [], 'lodge': []}
    letters = 'abcdefghijklmnopqrstuvwxyz'

    with open('words_alpha.txt') as fd:
        dictionary = set(
            filter(lambda wd: (4 < len(wd) < 7), [x.strip() for x in fd]))
        five_letters = set()
        six_letters = set()
        for word in dictionary:
            if len(word) == 5:
                five_letters.add(word)
            else:
                six_letters.add(word)
        # print(six_letters)

        for word in base_words:
            for letter in letters:
                new_word = word[0] + letter + word[2:]
                if new_word != word and new_word in five_letters:
                    print(f'{word} -> {new_word}')
                    base_words[word].append(letter)

        print(base_words)
        for a in base_words['stamp']:
            for b in base_words['curry']:
                for c in base_words['aches']:
                    for d in base_words['snack']:
                        for e in base_words['broom']:
                            for f in base_words['lodge']:
                                test_word = a+b+c+d+e+f
                                if test_word in six_letters:
                                    print(test_word)
