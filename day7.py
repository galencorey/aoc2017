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
    def __init__(self, name, weight, children):
        self.name = name
        self.weight = weight
        self.children = children
        self.total_weight = weight
    def add_total_weight(self, weight):
        self.total_weight = weight

def create_program_nodes(node_list):
    created = {}
    for node in node_list:
        pattern = re.compile('([a-z]+) \((\d+)\)(?: \-\> (.+))?')
        parsed_input = pattern.match(node)
        name = parsed_input.group(1)
        weight = int(parsed_input.group(2))
        children = None
        if (parsed_input.group(3) is not None):
            children = parsed_input.group(3).split(', ')
        if (name not in created):
            created[name] = program_node(name, weight, children)
    return created


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
# print(prog)

#program nodes is our "tree", can be used to get a node object from the name
program_nodes = create_program_nodes(input)

def collect_weights(base):
    weights = []
    if (base.children is not None):
        for child in base.children:
            child_node = program_nodes[child]
            weight = child_node.weight
            if (child_node.children is not None):
                weight += sum(collect_weights(child_node))
            child_node.add_total_weight(weight)
            weights.append(weight)
    return weights

def maybe_this_is_what_part_2_is_looking_for(base):
    # if (base.children is not None):
        num_children = len(base.children)
        #find odd child out
        odd_child_out = None
        normal_child = None
        for i in range(num_children):
            curr_child = program_nodes[base.children[i]]
            next_child = program_nodes[base.children[(i + 1) % num_children]]
            next_next_child = program_nodes[base.children[(i + 2) % num_children]]
            if (curr_child.total_weight != next_child.total_weight and next_child.total_weight == next_next_child.total_weight):
                odd_child_out = curr_child
                normal_child = next_child
        if (odd_child_out is not None):
            #is this the level where the weights are wonky?
            if (odd_child_out.weight != normal_child.weight):
                goal_weight = normal_child.total_weight
                odd_child_children_weight = odd_child_out.total_weight - odd_child_out.weight
                return goal_weight - odd_child_children_weight
            else:
                return maybe_this_is_what_part_2_is_looking_for(odd_child_out)

    #find odd one out
    #if direct child node has different weight than sibling, return that child's weight + 5
    #else repeat


print(maybe_this_is_what_part_2_is_looking_for(program_nodes['gmcrj']))
# print(collect_weights(program_nodes['gmcrj']))
# print(program_nodes['gmcrj'].children)
# print(program_nodes['gejdtfw'].weight)
