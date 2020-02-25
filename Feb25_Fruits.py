# In each of the 5 words, can you change the uppercase letter
# to produce 5 new words.

# Date
# nUt
# Lime
# pEach
# Pear

# The new letters spell a fruit.

def count_with_carry(data):
    data_len = len(data)
    indexes = [0 for x in range(0, data_len)]
    curr_incr = data_len - 1
    while indexes[0] < len(data[0]):
        word = ''
        for x in range(0, data_len):
            word += data[x][indexes[x]]
        yield word

        while curr_incr > -1:
            indexes[curr_incr] += 1
            if curr_incr > 0 and indexes[curr_incr] >= len(data[curr_incr]):
                indexes[curr_incr] = 0
                curr_incr -= 1
            else:
                break
        curr_incr = data_len - 1


if __name__ == '__main__':
    alphabet = list('abcdefghijklmonpqrstuvwxyz')
    words = [
        ('?ate', 'd'),
        ('n?t', 'n'),
        ('?ime', 'l'),
        ('p?ach', 'e'),
        ('?ear', 'p')
    ]
    with open('20k.txt') as fd:
        dictionary = set(
            filter(lambda wd: (len(wd) >= 3 and len(wd) <= 6), [x.strip() for x in fd]))
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
        # print(new_letter_options)

        for new_word in count_with_carry(new_letter_options):
            if new_word in dictionary:
                print(new_word)
