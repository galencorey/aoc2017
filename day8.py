import re

input_file = open('day8input.txt', 'r')
input = input_file.read().strip().split('\n')

class register:
    def __init__(self, name):
        self.name = name
        self.value = 0
    def inc(self, amt):
        self.value += amt
    def dec(self, amt):
        self.value -= amt
    def __getitem__(self, item):
        return getattr(self, item)

def build_registers_from_input(inputs):
    #make all instances of registers and store them
    registers = {}
    for input in inputs:
        match = re.match('[a-z]+', input)
        name = match.group(0)
        registers[name] = register(name)
    return registers

def find_largest_register(registers):
    max = None
    for register in registers:
        if (max is None or registers[register].value > max):
            max = registers[register].value
    return max

def run_all_commands(inputs):
    registers = build_registers_from_input(inputs)
    for input in inputs:
        pattern = re.compile('([a-z]+) ([a-z]+) ([-\d]+) if ([a-z]+)(.+)')
        parsed_input = pattern.match(input)
        print(input)
        if (parsed_input is not None):
            #parse input
            name_of_register_to_change = parsed_input.group(1)
            change_method = parsed_input.group(2)
            change_amount = int(parsed_input.group(3))
            name_of_register_to_check = parsed_input.group(4)
            check_expression = parsed_input.group(5)

            #see if condition is met
            if(name_of_register_to_check in registers):
                check_val = registers[name_of_register_to_check].value
                expression_string = str(check_val) + check_expression
                if(eval(expression_string)):
                    #do correct operation
                    register = registers[name_of_register_to_change]
                    register[change_method](change_amount)
    return find_largest_register(registers)

print(run_all_commands(input))
