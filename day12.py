import re

input_file = open('day12input.txt', 'r')
input = input_file.read().strip().split('\n')

class proggy:
    def __init__(self, input_str):
        match = re.match('(.+) <-> (.+)', input_str)
        self.name = match.group(1)
        self.neighbors = match.group(2).split(', ')

def create_proggy_dict(input):
    proggys = {}
    for input_str in input:
        progster = proggy(input_str)
        proggys[progster.name] = progster
    return proggys

all_proggys = create_proggy_dict(input)

added = []
def gather_neighbors(proggy):
    neighbors = proggy.neighbors
    neighbors.append(proggy.name)
    if (proggy.name not in added):
        added.append(proggy.name)
        for n in proggy.neighbors:
            if (n not in added):
                neighbor_prog = all_proggys[n]
                superneighbors = gather_neighbors(neighbor_prog)
                neighbors = list(set(neighbors) | set(superneighbors))
                added.append(n)

    return neighbors

print(len(gather_neighbors(all_proggys['0'])))
# print(all_proggys['0'])
