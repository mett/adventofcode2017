""" balance.py
Implementation of tree balancer for day 7 of advent of code.
"""


class Node(object):
    def __init__(self, name, weight, connections=None):
        self.name = name
        self.weight = weight
        self.connections = connections

    def __repr__(self):
        return self.name


def generate_tree(indata):
    with open(indata, 'r') as tree_input:
        branches = dict()
        leaves = dict()
        for line in tree_input:
            if '->' in line:
                [leaf_info, connections] = line.split('->')
            else:
                leaf_info = line
                connections = None
            [name, dirty_weigth] = leaf_info.split()
            weight = dirty_weigth.strip('()')

            if not connections:
                if weight not in leaves:
                    leaves[name] = [Node(name, weight)]
                else:
                    leaves[weight].append(Node(name, weight))
            else:
                if weight not in branches:
                    branches[weight] = [Node(name, weight, connections)]
                else:
                    branches[weight].append(Node(name, weight, connections))
    print leaves
    print branches
