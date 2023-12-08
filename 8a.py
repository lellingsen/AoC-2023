from aoc import get_input

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

current_node = 'AAA'
steps = 0
while True:
    i = steps % len(instructions)
    if instructions[i] == 'L':
        current_node = nodes[current_node]['left']
    else:
        current_node = nodes[current_node]['right']
    
    steps += 1
    if current_node == 'ZZZ':
        break

print(steps)
