from aoc import get_input
import math

input = get_input(8).splitlines()

instructions = input[0]

nodes = {}
for line in input[1:]:
    if line == '':
        continue
    line_contents = line.split(' = ')
    node_id = line_contents[0]
    left_and_right = line_contents[1].split(', ')
    left = left_and_right[0].replace('(', '')
    right = left_and_right[1].replace(')', '')
    nodes[node_id] = { 'left': left, 'right': right }

current_nodes = [key for key in nodes.keys() if key.endswith('A')]
# Need to track how many steps it takes to get to the end for each starting node
# Then we can calculate the least common multiple for them
steps_to_end = [0] * len(current_nodes)
steps = 0
while True:
    instr = steps % len(instructions)
    steps += 1
    new_nodes = []
    for i, current_node in enumerate(current_nodes):
        if instructions[instr] == 'L':
            current_nodes[i] = nodes[current_node]['left']
        else:
            current_nodes[i] = nodes[current_node]['right']

        if steps_to_end[i] == 0 and current_nodes[i].endswith('Z'):
            steps_to_end[i] = steps
    
    if all(steps != 0 for steps in steps_to_end):
        break

print(math.lcm(*steps_to_end))
