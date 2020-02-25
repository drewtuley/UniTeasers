# In each of the 5 words, can you change the uppercase letter
# to produce 5 new words.

# Date
# nUt
# Lime
# pEach
# Pear

# The new letters spell a fruit.

if __name__ == '__main__':
    alphabet = list('abcdefghijklmonpqrstuvwxyz')
    words = [
        ('?ate', 'd'),
        ('n?t','n'),
        ('?ime','l'),
        ('p?ach', 'e'),
        ('?ear', 'p')
    ]
    with open('20k.txt') as fd:
        dictionary = set(
            filter(lambda wd: (len(wd) >= 3 and len(wd)<=6), [x.strip() for x in fd]))
        new_letter_options = []
        for word in words:
            hit_letters = []
            for letter in alphabet:
                if letter != word[1]:
                    test_word = word[0].replace('?', letter)
                    if test_word in dictionary:
                        hit_letters.append(letter)
                        print(test_word)
            new_letter_options.append(hit_letters)
        #print(new_letter_options)
        for a in new_letter_options[0]:
            for b in new_letter_options[1]:
                for c in new_letter_options[2]:
                    for d in new_letter_options[3]:
                        for e in new_letter_options[4]:
                            word = a+b+c+d+e
                            if word in dictionary:
                                print(word)

