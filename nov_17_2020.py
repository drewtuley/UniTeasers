from itertools import permutations

source_words = ['HERB','BANG','KEEN','SUIT','QUAD','WHEY','CELL','TOIL','WILD']
if __name__ == '__main__':
    five_letter_words = []
    nine_letter_words = []
    with open('words_alpha.txt') as fd:
        for rword in fd:
            word = rword.strip()
            if len(word)  == 5:
                five_letter_words.append(word.upper())
            elif len(word) == 9:
                nine_letter_words.append(word.upper())

        possibles = []
        for sword in source_words:
            new_words = set()
            possible_letters = set()
            for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                new_word = sword+letter
                for rcombo in permutations(new_word, 5):
                    combo = ''.join(rcombo)
                    if combo in five_letter_words and combo not in new_words:
                        print(f'{sword}+{letter}={combo}')
                        new_words.add(combo)
                        possible_letters.add(letter)
            possibles.append(possible_letters)
        print(possibles)

        for a in possibles[0]:
            for b in possibles[1]:
                for c in possibles[2]:
                    for d in possibles[3]:
                        for e in possibles[4]:
                            for f in possibles[5]:
                                for g in possibles[6]:
                                    for h in possibles[7]:
                                        for i in possibles[8]:
                                           if a+b+c+d+e+f+g+h+i in nine_letter_words:
                                                print(a+b+c+d+e+f+g+h+i)
