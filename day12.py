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
# part 1
# print(len(gather_neighbors(all_proggys['0'])))

def count_groups(proggydict):
    accounted_for = []
    num_groups = 0
    for name, proggy in proggydict.items():
        if (name not in accounted_for):
            accounted_for = accounted_for + gather_neighbors(proggy)
            num_groups += 1
    print(accounted_for)
    return num_groups


print(count_groups(all_proggys))
