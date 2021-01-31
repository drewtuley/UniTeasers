from itertools import permutations


# See file://may_17.jpg


class Skater():
    def __init__(self, name, age, colour, position):
        self.name = name
        self.age = age
        self.colour = colour
        self.position = position

    def __str__(self):
        return f'Position: {self.position} Name: {self.name:6} Age: {self.age} Colour: {self.colour} '


if __name__ == '__main__':
    for age in permutations([18, 21, 24, 28]):
        for colour in permutations(['blue', 'red', 'green', 'yellow']):
            for position in permutations([1, 2, 3, 4]):
                jesse = Skater('Jesse', age[0], colour[0], position[0])
                kelly = Skater('Kelly', age[1], colour[1], position[1])
                logan = Skater('Logan', age[2], colour[2], position[2])
                max = Skater('Max', age[3], colour[3], position[3])
                skater_by_name={}
                skater_by_age = {}
                skater_by_colour = {}
                skater_by_position = {}
                for skater in [jesse, kelly, logan, max]:
                    skater_by_name[skater.name] = skater
                    skater_by_age[skater.age] = skater
                    skater_by_colour[skater.colour] = skater
                    skater_by_position[skater.position] = skater
                rule1 = skater_by_age[18].colour != 'blue' and skater_by_age[18].position == 1
                rule2 = skater_by_name['Jesse'].age == skater_by_colour['red'].age - 3
                rule3 = skater_by_name['Kelly'].position == 2
                rule4 = skater_by_name['Logan'].colour == 'green' and skater_by_name['Max'].age == 28
                rule5 = skater_by_colour['yellow'].age < skater_by_name['Kelly'].age and skater_by_position[4].age == 21
                if all(rule for rule in [rule1, rule2, rule3, rule4, rule5]):
                    for pos in [1,2,3,4]:
                        print(skater_by_position[pos])
