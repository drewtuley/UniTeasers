import re

the_riddle = '''
My First is in horse but not in pony
My Second is in coyote but not in jackal
My third is in shrew and also in vole
My Fourth is in panda but not in bear
My last is in baboon but not in monkey
What am I?
'''

ordinals = {'first': 0, 'second': 1, 'third': 2, 'fourth': 3, 'fifth': 4, 'sixth': 5, 'seventh': 6, 'last': 99}


def parse_riddle(riddle):
    p = re.compile(r'my (?P<ordinal>\w+) is in (?P<first>\w+) (?P<clause>but not in|and also in) (?P<second>\w+)')

    letters_list = {}
    for match in p.finditer(riddle.lower()):
        ordinal = match.group('ordinal')
        ordinal_index = ordinals[ordinal]
        if match.group('clause') == 'but not in':
            these_letters = set(filter(lambda letter: (letter not in match.group('second')), match.group('first')))
        else:
            these_letters = set(filter(lambda letter: (letter in match.group('second')), match.group('first')))
        letters_list[ordinal_index] = these_letters
    return [letters_list[x] for x in sorted(letters_list.keys())]


def find_word(target_word, index, lists):
    if index < len(lists):
        for letter in lists[index]:
            new_target = target_word + letter
            yield from find_word(new_target, index + 1, lists)
    else:
        yield target_word


if __name__ == '__main__':
    possible_letters_lists = parse_riddle(the_riddle)

    word_len = len(possible_letters_lists)
    with open('20k.txt') as fd:
        dictionary = set(filter(lambda x: (len(x) == word_len), [x.strip() for x in fd]))

        print('Loaded {:,} {} letter words into dictionary'.format(len(dictionary), word_len))

        found_words = list(filter(lambda testword: (testword in dictionary), find_word('', 0, possible_letters_lists)))
        if len(found_words) > 0:
            print(the_riddle)
            print('I am a {}'.format(found_words[0]))
