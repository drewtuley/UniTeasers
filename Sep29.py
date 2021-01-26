# Playgroup teddies

from itertools import permutations


class Child(object):
    age = None
    teddy_count = None
    name = None

    def __init__(self, age, name, teddy_count):
        self.age = age
        self.name = name
        self.teddy_count = teddy_count

    def __str__(self):
        return f'Name: {self.name} age: {self.age} teddies: {self.teddy_count}'


if __name__ == '__main__':
    kids = ['Dale', 'Jesse', 'Morgan', 'Pat']
    for ages, teddies in permutations(permutations(range(1, 5)), 2):
        aged_children = []
        for idx in range(0, 4):
            c = Child(ages[idx], kids[idx], teddies[idx])
            aged_children.append(c)

            # print(f'{aged_children[0]} {aged_children[1]} {aged_children[2]} {aged_children[3]}')
        kiddies = {}
        for ac in aged_children:
            kiddies[ac.name] = ac
            # print(kiddies)
        if kiddies['Dale'].teddy_count > kiddies['Dale'].age and kiddies['Jesse'].age > kiddies['Morgan'].age and \
                kiddies['Pat'].age == 1 and kiddies['Pat'].teddy_count < kiddies['Jesse'].teddy_count:
            for ac in aged_children:
                if ac.age == 3 and ac.teddy_count == 2:
                    teddies_same_age = 0
                    for ac2 in aged_children:
                        if ac2.age == ac2.teddy_count:
                            teddies_same_age += 1
                    if teddies_same_age == 1:
                        print(f'{aged_children[0]}\n{aged_children[1]}\n{aged_children[2]}\n{aged_children[3]}')
