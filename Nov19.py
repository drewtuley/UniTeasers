import re

the_riddle = '''
My First is in horse but not in pony
My Second is in coyote but not in jackal
My third is in shrew and also in vole
My Fourth is in panda but not in bear
My last is in baboon but not in monkey
What am I?
'''

ordinals = {'first': 1, 'second': 2, 'third': 3, 'fourth': 4, 'fifth': 5, 'sixth': 6, 'seventh': 7, 'last': 999}


# break down the riddle into lines composed of the following form:
# my <letter_position> is in <word> (but not OR and also) in <word>
# from each line obtain a list of possible letters that could match the target letter in that position
def parse_riddle(riddle):
    p = re.compile(r'my (?P<ordinal>\w+) is in (?P<first>\w+) (?P<clause>but not|and also) in (?P<second>\w+)')

    letters_list = {}
    # the following is pretty brittle, if the input line is not in the correct format it will be ignored
    for match in p.finditer(riddle.lower()):
        # index_by_ordinal is the position that this line represents in the target word
        # it would allow (if we wanted) the riddle to mix up the lines and still work
        # (i.e. if 'My third ...' comes before 'My first..')
        index_by_ordinal = ordinals[match.group('ordinal')]
        if match.group('clause') == 'but not':
            these_letters = set(filter(lambda letter: (letter not in match.group('second')), match.group('first')))
        else:
            these_letters = set(filter(lambda letter: (letter in match.group('second')), match.group('first')))
        letters_list[index_by_ordinal] = these_letters
    # return a list of possible letters for each position (sorted into the correct order)
    return [letters_list[x] for x in sorted(letters_list.keys())]


# recursively generate 'words' from each of the possible letters at each position
def find_words(target_word, letter_position_index, lists):
    if letter_position_index < len(lists):
        for letter in lists[letter_position_index]:
            new_target = target_word + letter
            yield from find_words(new_target, letter_position_index + 1, lists)
    else:
        yield target_word


if __name__ == '__main__':
    possible_letters_lists = parse_riddle(the_riddle)

    word_len = len(possible_letters_lists)
    with open('20k.txt') as fd:
        # create a dictionary of words the same length as the word we're looking for
        dictionary = set(filter(lambda x: (len(x) == word_len), [x.strip() for x in fd]))

        print('Loaded {:,} {} letter words into dictionary'.format(len(dictionary), word_len))

        found_words = list(
            filter(lambda test_word: (test_word in dictionary), find_words('', 0, possible_letters_lists)))
        if len(found_words) > 0:
            print(the_riddle)
            print('I am a {}'.format(found_words[0]))
