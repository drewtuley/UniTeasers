from itertools import permutations
from requests import head


def test_words_on_wiktionary(words, valid_words):
    invalid_words = []
    print('Test words: ' + ','.join(words))
    for word_to_test in words:
        if word_to_test not in valid_words:
            r = head('https://en.wiktionary.org/wiki/' + word_to_test)
            if r.status_code != 200:
                invalid_words.append(word_to_test)
            else:
                valid_words.append(word_to_test)

    return invalid_words


if __name__ == '__main__':
    test = test_words_on_wiktionary(['snap', 'nape', 'apes', 'pest'], [])
    if len(test) == 0:
        print('test passes OK')
    else:
        print('Fail: Those words should pass OK')
        exit(1)

    invalid_word_cache = []
    valid_word_cache = []
    for p in permutations(['a', 'e', 'n', 'p', 'p', 's']):
        words_to_test = [
            's' + p[0] + p[1] + p[2],
            p[0] + 'a' + p[3] + p[4],
            p[1] + p[3] + 'e' + p[5],
            p[2] + p[4] + p[5] + 't'
        ]

        if not any(word in invalid_word_cache for word in words_to_test):
            bad_words = test_words_on_wiktionary(words_to_test, valid_word_cache)
            if len(bad_words) == 0:
                print(words_to_test)
                break
            else:
                invalid_word_cache.extend(bad_words)
