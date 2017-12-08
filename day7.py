import re

input_file = open('day7input.txt', 'r')
input = input_file.read().strip().split('\n')

#
# class program_node:
#     def __init__(self, name, ):
#         pattern = re.compile('([a-z]+) \((\d+)\)(?: \-\> (.+))?')
#         parsed_input = pattern.match(input_str)
#         if (parsed_input is not None):
#             self.name = parsed_input.group(1)
#             self.weight = int(parsed_input.group(2))
#             if (parsed_input.group(3) is not None):
#                 self.children = parsed_input.group(3).split(', ')
#             else:
#                 self.children = None

class program_node:
    def __init__(self, name, weight, children, parent):
        self.name = name
        self.weight = weight
        self.children = children
        self.parent = parent
    def add_parent(self, parent):
        self.parent = parent

# def create_nodes(node_list):
#     created = {}
#     for node in node_list:
#         pattern = re.compile('([a-z]+) \((\d+)\)(?: \-\> (.+))?')
#         parsed_input = pattern.match(node)
#         name = parsed_input.group(1)
#         weight = int(parsed_input.group(2))
#         children = None
#         if (parsed_input.group(3) is not None):
#             children = parsed_input.group(3).split(', ')
#         if (name not in created):
#             created[name] = program_node()

def find_base_program(input_list):
    all_programs = []
    child_programs = []
    for input in input_list:
        pattern = re.compile('([a-z]+) \((\d+)\)(?: \-\> (.+))?')
        parsed_input = pattern.match(input)
        name = parsed_input.group(1)
        all_programs.append(name)
        if (parsed_input.group(3) is not None):
            children = parsed_input.group(3).split(', ')
            child_programs += children
    return set(all_programs) - set(child_programs)

# prog = find_base_program(['xhth (57)', 'ebii (61)', 'havc (66)', 'ktlj (57)', 'fwft (72) -> ktlj, cntj, xhth', 'qoyq (66)', 'padx (45) -> pbga, havc, qoyq', 'tknk (41) -> ugml, padx, fwft', 'jptl (61)', 'ugml (68) -> gyxo, ebii, jptl', 'gyxo (61)', 'cntj (57)'])

prog = find_base_program(input)

print(prog)
