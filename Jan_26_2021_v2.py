import copy
import re


class Vertex(object):
    def __init__(self, node1, node2):
        self.node1 = node1
        self.node2 = node2

    def __hash__(self):
        return hash(self.node1.letter) ^ hash(self.node2.letter)

    def __repr__(self):
        return f'{self.node1},{self.node2}'


class Node(object):
    edges = set()

    def __init__(self, letter):
        self.letter = letter[0]

    def __repr__(self):
        return f'{self.letter}'

    def join_node(self, other):
        self.edges.add(Vertex(self, other))

    def get_joined_nodes(self):
        for vertex in self.edges:
            if vertex.node1 == self:
                yield vertex.node2
            elif vertex.node2 == self:
                yield vertex.node1


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
        # print(word_stream)
        if len(word_stream) == 20:
            possibles.append(word_stream)


def add_edge(edge, nodes):
    try:
        edge1 = nodes[edge[0]]
    except KeyError:
        edge1 = Node(edge[0])
        nodes[edge[0]] = edge1

    try:
        edge2 = nodes[edge[1]]
    except KeyError:
        edge2 = Node(edge[1])
        nodes[edge[1]] = edge2
    edge1.join_node(edge2)
    # edge2.join_node(edge1)


if __name__ == '__main__':
    nodes = {}
    with open('Jan262021_edges.txt') as fd:
        for l in fd:
            edge = re.search(r'^(?P<v1>[A-Za-z][0-9]*),(?P<v2>[A-Za-z][0-9]*)$', l.strip())
            if edge is not None:
                v1 = edge.group('v1')
                v2 = edge.group('v2')
                # print(f'{v1} {v2}')
                add_edge((v1, v2), nodes)

        likely = list()
        traverse_nodes(nodes['t'], nodes['y'], [], set(), likely)
        print(likely)
