from itertools import permutations

# See oct_29_2020.jpg


class Sweet(object):
    colour = None

    def __init__(self, colour):
        self.colour = colour

    def __repr__(self):
        return f'{self.colour}'

    def __eq__(self, other):
        return self.colour == other.colour

    def is_colour(self, colour):
        return self.colour == colour

    def __lt__(self, other):
        return self.colour < other.colour

    def __hash__(self):
        return hash(self.colour)


class Child(object):
    name = None
    sweet1 = None
    sweet2 = None

    def __init__(self, name, sweet1, sweet2):
        self.name = name
        self.sweet1 = sweet1
        self.sweet2 = sweet2

    def has_colour(self, colour):
        return self.sweet1.is_colour(colour) or self.sweet2.is_colour(colour)

    def __repr__(self):
        return f'{self.name:8}: has - {self.sweet1},{self.sweet2}'

    def __hash__(self):
        return hash(self.name) ^ hash(self.sweet1) ^ hash(self.sweet2)

    def __eq__(self, other):
        return self.name == other.name and self.sweet1 == other.sweet1 and self.sweet2 == other.sweet2


class Solution(object):
    solution_children = []

    def __init__(self, children):
        self.solution_children = [c for c in children]

    def __repr__(self):
        return f'{self.solution_children[0]}\n{self.solution_children[1]}\n{self.solution_children[2]}\n{self.solution_children[3]}'

    def __eq__(self, other):
        return self.solution_children[0] == other.solution_children[0] and self.solution_children[1] == \
               other.solution_children[1] and self.solution_children[2] == \
               other.solution_children[2] and self.solution_children[3] == other.solution_children[3]

    def __hash__(self):
        return self.solution_children[0].__hash__() ^ self.solution_children[1].__hash__() ^ self.solution_children[
            2].__hash__() ^ self.solution_children[
                   3].__hash__()


if __name__ == '__main__':
    sweets = [Sweet('blue'), Sweet('blue'), Sweet('red'), Sweet('red'), Sweet('green'), Sweet('green'), Sweet('orange'),
              Sweet('orange')]
    solutions = set()
    for s1, s2, s3, s4, s5, s6, s7, s8 in permutations(sweets, 8):
        if s1 < s2 and s3 < s4 and s5 < s6 and s7 < s8:
            jesse = Child('Jesse', s1, s2)
            jamie = Child('Jamie', s3, s4)
            jo = Child('Jo', s5, s6)
            jules = Child('Jules', s7, s8)

            if not jules.has_colour('orange') and not jesse.has_colour('blue') and not jamie.has_colour(
                    'red') and jo.has_colour('green') and jesse.has_colour('orange'):
                children = [jesse, jamie, jo, jules]
                x1 = set(filter(lambda child: (child.has_colour('red') and child.has_colour('green')), children))
                x2 = set(filter(lambda child: (child.has_colour('red') and child.has_colour('blue')), children))
                if len(x1) >= 1 and len(x2) == 1:
                    solutions.add(Solution(children))

    for s in solutions:
        print(s)
