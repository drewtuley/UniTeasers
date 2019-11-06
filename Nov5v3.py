import threading


import requests

# Safari Animals
# Below are safari animals, however, each letter has been replaced by its position in the alphabet,
# but the spaces between the resulting numbers have been removed.
# e.g. DOG=4.15.7=4157

animals = [
    '18891415',
    '3181531549125',
    '79181665',
    '38552018',
    '12515161184',
    '89161615',
    '512516811420',
    '2216611215',
    '1291514'
]


def recursive_parse(numeric_word, parsed_word, current_index, max_index, parsed_list):
    while current_index < max_index:
        numeric_letter = numeric_word[current_index]
        # if the next number is 0 it must be part of this 'numeric letter'
        if current_index + 1 < max_index and numeric_word[current_index + 1] == '0':
            numeric_letter += '0'
            current_index += 1
        # if the current 'numeric letter' is 1 or 2 AND there are more numbers
        # it _may_ be a 2 digit numeric letter
        if numeric_letter in ['1', '2'] and current_index + 1 < max_index:
            next_letter = numeric_word[current_index + 1]
            test_letter = int(numeric_letter + next_letter)
            save_word = parsed_word
            if test_letter < 27:
                parsed_word += chr(test_letter + 64)
                recursive_parse(numeric_word, parsed_word, current_index + 2, max_index,
                                parsed_list)
                parsed_word = save_word
        parsed_word += chr(int(numeric_letter) + 64)
        current_index += 1
    parsed_list.append(parsed_word[0] + parsed_word[1:].lower())


def parse(number_word):
    parsed_word = ''
    current_index = 0
    parsed_list = []
    max_index = len(number_word)
    recursive_parse(number_word, parsed_word, current_index, max_index, parsed_list)
    return parsed_list


def ask_wikipedia(lock, animal, parsed_animal_list):
    for parsed_animal in parsed_animal_list:
        # ask Wikipedia if it knows what the animal is
        r = requests.head('https://en.wikipedia.org/wiki/' + parsed_animal)
        if r.status_code == 301:
            # if wikipedia gives us a redirect, pick up the new location and try that
            r = requests.head(r.headers['Location'])
        if r.status_code == 200:
            lock.acquire()
            print('{} = {} (out of {} choices)'.format(animal, parsed_animal, len(parsed_animal_list)))
            lock.release()
            break


lock = threading.Lock()
for animal in animals:
    parsed_animal_list = parse(animal)
    # print(parsed_animal_list)
    find = threading.Thread(target=ask_wikipedia, args=(lock, animal, parsed_animal_list))
    find.start()
