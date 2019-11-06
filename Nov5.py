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

for animal in animals:
    current_index = 0
    generated_name = ''
    max_index = len(animal)
    while current_index < max_index:
        number_letter = animal[current_index]
        if 1 == 2 and number_letter in ['1', '2'] and current_index + 1 < max_index:
            next_number_letter = animal[current_index + 1]
            test_word = int(number_letter + next_number_letter)
            if test_word < 27:
                letter = chr(test_word + 64)
                generated_name += letter
            current_index += 2
        else:
            if current_index + 1 < max_index and animal[current_index + 1] == '0':
                test_word = int(animal[current_index:current_index + 2])
                current_index += 1
            else:
                test_word = int(number_letter)
            letter = chr(test_word + 64)
            generated_name += letter
            current_index += 1
    generated_name = generated_name[0] + generated_name[1:].lower()
    print(generated_name)
    r = requests.head('https://en.wikipedia.org/wiki/' + generated_name.lower())
    if r.status_code == 301:
        new_location = r.headers['Location']
        r = requests.head(new_location)
    if r.status_code == 200:
        print('{} = {}'.format(animal, generated_name))
    else:
        print(r)
