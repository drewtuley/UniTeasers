class Sub(object):
    text = None

    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return f'{self.text}'

    def __hash__(self):
        return hash(self.text)

    def __eq__(self, other):
        return self.text == other.text
    

class Test(object):
    id = None
    sub = None

    def __init__(self, id, text):
        self.id = id
        self.sub = Sub(text)

    def __repr__(self):
        return f'{self.id}:{self.sub}({self.__hash__()})'

    def __eq__(self, other):
        return self.id == other.id and self.sub == other.sub

    def __lt__(self, other):
        return self.id < other.id

    def __hash__(self):
        return hash(self.id) ^ hash(self.sub)


if __name__ == '__main__':
    s = set()
    s.add(Test(1, 'aa'))
    s.add(Test(2, 'bb'))
    s.add(Test(1, 'cc'))
    s.add(Test(1, 'aa'))

    print(sorted(s))
