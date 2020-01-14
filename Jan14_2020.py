from itertools import permutations

# A to Z
# Complete these 'common words' by using all of the letters A to Z, each exactly once.
common_words = [
    '??eue',
    '???k?am?on',
    '?p?a?e?',
    '?erso?',
    '???igent',
    '?ouse',
    '?ur?',
    '?e?er',
    '??o',
    'ma?',

    '?a?'
]
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']


def replace_wildcards(source_word, replacements):
    return_word = ''
    replaced_letters = ''
    index = 0
    for letter in source_word:
        if letter == '?':
            return_word += replacements[index]
            replaced_letters += replacements[index]
            index += 1
        else:
            return_word += letter
    return return_word, replaced_letters


def count_wildcards(test_word):
    wildcard_count = 0
    for letter in test_word:
        if letter == '?':
            wildcard_count += 1
    return wildcard_count


def remove_letters(letters_to_remove):
    for to_remove in letters_to_remove:
        letters.remove(to_remove)


if __name__ == '__main__':
    with open('20k.txt') as fd:
        dictionary = set(
            filter(lambda wd: (len(wd) >= 3 and wd not in ['youse', 'wat', 'wav', 'max']), [x.strip() for x in fd]))

        winning_words = {}
        matched = {}
        for word in common_words:
            # for each word in the 'common word' list replace the wildcards
            # with all possible permutations from the remaining letters in the letter pool
            wildcards = count_wildcards(word)
            list_of_replacements = []
            for seq in permutations(letters, wildcards):
                new_word, replacement_letters = replace_wildcards(word, seq)
                if new_word in dictionary:
                    list_of_replacements.append(replacement_letters)
            matched[word] = list_of_replacements
            if len(list_of_replacements) == 1:
                # if, for a given word there was only ONE set of replacement letters
                # we have a match. So log the match and remove the replacement letters from the letter pool
                new_word = replace_wildcards(word, list_of_replacements[0])
                winning_words[word] = new_word[0]
                remove_letters(list_of_replacements[0])

        if len(winning_words) > 0:
            # remove any found words from the matched data set
            for word in winning_words:
                matched.pop(word)

            for letter in letters:
                # for each of the remaining letters in the letter pool
                # determine if it is used by only one of the common words
                possible_replacements = []
                for matched_wildcard in matched:
                    for replacements in matched[matched_wildcard]:
                        if letter in replacements:
                            possible_replacements.append((replacements, matched_wildcard))
                if len(possible_replacements) == 1:
                    # if so, log the match and then remove that letter from the pool
                    new_word = replace_wildcards(possible_replacements[0][1], possible_replacements[0][0])
                    winning_words[possible_replacements[0][1]] = new_word[0]
                    matched.pop(possible_replacements[0][1])
                    remove_letters(possible_replacements[0][0])

        for word in winning_words:
            print('{0}->{1}'.format(word, winning_words[word]))

        multiple = 1
        for seq in permutations(letters, len(letters)):
            idx = 0
            optional_list = {}
            for matched_wildcard in matched:
                wildcards = count_wildcards(matched_wildcard)
                replacements = seq[idx: idx + wildcards]
                new_word = None
                for r in matched[matched_wildcard]:
                    if ''.join(replacements) in r:
                        new_word = replace_wildcards(matched_wildcard, replacements)
                        optional_list[matched_wildcard] = new_word[0]
                        idx += wildcards
                        break
                if new_word is None:
                    break
            if len(optional_list) == len(matched):
                print('Multiple: #{}'.format(multiple))
                for word in optional_list:
                    print(' {0}->{1}'.format(word, optional_list[word]))
                multiple += 1
