import copy


class Vertex(object):
    def __init__(self, node1, node2):
        self.node1 = node1
        self.node2 = node2

    def __lt__(self, other):
        return self.node1 < other.node1 and self.node2 < other.node2


class Node(object):
    vertices = set()

    def __init__(self, letter):
        self.letter = letter

    def join_node(self, other):
        v = Vertex(self, other)
        self.vertices.add(v)

    def get_joined_nodes(self):
        for vertex in self.vertices:
            if vertex.node1 == self:
                yield vertex.node2
            elif vertex.node2 == self:
                yield vertex.node1


if __name__ == '__main__':
    vertices = set()

    t = Node('t')
    h = Node('h')
    t.join_node(h)
    o = Node('o')
    n = Node('n')
    n.join_node(o)
    i = Node('i')
    e = Node('e')
    h.join_node(o)
    h.join_node(n)
    h.join_node(i)
    h.join_node(e)

    p = Node('p')
    o.join_node(p)
    n.join_node(p)

    o2 = Node('o')
    p.join_node(o2)
    n.join_node(o2)

    s = Node('s')
    o2.join_node(s)
    n.join_node(s)

    s2 = Node('s')
    n.join_node(s2)
    i.join_node(s2)

    b = Node('b')
    s.join_node(b)
    s2.join_node(b)

    s3 = Node('s')
    s.join_node(s3)
    b.join_node(s3)

    i2 = Node('i')
    s3.join_node(i2)
    b.join_node(i2)

    y = Node('y')
    b.join_node(y)
    i2.join_node(y)

    e2 = Node('e')
    i.join_node(e2)

    l1 = Node('l')
    b.join_node(l1)

    e3 = Node('e')
    i.join_node(e3)
    l1.join_node(e3)

    r = Node('r')
    e.join_node(r)
    i.join_node(r)
    e2.join_node(r)

    w = Node('w')
    e3.join_node(w)
    e2.join_node(w)
    l1.join_node(w)

    a = Node('a')
    w.join_node(a)
    y.join_node(a)
    y.join_node(w)


    def traverse_nodes(current, end, letters, visited_nodes, possibles):
        my_letters = copy.copy(letters)
        my_letters.append(current.letter)
        my_visited_nodes = copy.copy(visited_nodes)
        my_visited_nodes.add(current)
        if current != end:
            for node in current.get_joined_nodes():
                if node not in my_visited_nodes:
                    traverse_nodes(node, end, my_letters, my_visited_nodes, possibles)
        else:
            word_stream = ''.join(my_letters)
            if len(word_stream) == 20:
                possibles.append(word_stream)


    likely = list()
    traverse_nodes(t, y, [], set(), likely)
    print(likely)
