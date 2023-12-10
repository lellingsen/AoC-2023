from math import ceil
from aoc import get_input

input = get_input(10).splitlines()

# find starting point
starting_coords = None
for row, line in enumerate(input):
    column = line.find('S')
    if column != -1:
        starting_coords = (row, column)
        break

def get_initial_coords(starting_coords):
    def coord_in_bounds(coords):
        return coords[0] >= 0 and coords[1] >= 0 and coords[0] < len(input) and coords[1] < len(input[coords[0]])
    def is_connected_to_start(coords, possible_pipes):
        return (coord_in_bounds(coords) and 
            input[coords[0]][coords[1]] in possible_pipes)

    coord_above = (starting_coords[0] - 1, starting_coords[1], 'up')
    if is_connected_to_start(coord_above, ['|', 'F', '7']):
        return coord_above
    coord_left = (starting_coords[0], starting_coords[1] - 1, 'down')
    if is_connected_to_start(coord_left, ['-', 'F', 'L']):
        return coord_left
    coord_right = (starting_coords[0], starting_coords[1] + 1, 'right')
    if is_connected_to_start(coord_right, ['-', 'J', '7']):
        return coord_right
    return (starting_coords[0] + 1, starting_coords[1], 'left')

prev_coords = starting_coords
cur_coords = get_initial_coords(starting_coords)
cur_pipe = input[cur_coords[0]][cur_coords[1]]
steps = 0

def get_coords_for_direction(coords, direction):
    if direction == 'up':
        return (coords[0] - 1, coords[1], direction)
    elif direction == 'down':
        return (coords[0] + 1, coords[1], direction)
    elif direction == 'left':
        return (coords[0], coords[1] - 1, direction)
    return (coords[0], coords[1] + 1, direction)

while cur_pipe != 'S':
    steps += 1
    cur_direction = cur_coords[2]
    if cur_pipe == '|':
        next_coords = get_coords_for_direction(cur_coords, cur_coords[2])
    elif cur_pipe == '-':
        next_coords = get_coords_for_direction(cur_coords, cur_coords[2])
    elif cur_pipe == 'F':
        if cur_direction == 'up':
            next_coords = get_coords_for_direction(cur_coords, 'right')
        else:
            next_coords = get_coords_for_direction(cur_coords, 'down')
    elif cur_pipe == 'J':
        if cur_direction == 'down':
            next_coords = get_coords_for_direction(cur_coords, 'left')
        else:
            next_coords = get_coords_for_direction(cur_coords, 'up')
    elif cur_pipe == 'L':
        if cur_direction == 'left':
            next_coords = get_coords_for_direction(cur_coords, 'up')
        else:
            next_coords = get_coords_for_direction(cur_coords, 'right')
    else:
        if cur_direction == 'right':
            next_coords = get_coords_for_direction(cur_coords, 'down')
        else:
            next_coords = get_coords_for_direction(cur_coords, 'left')

    cur_coords = next_coords
    cur_pipe = input[cur_coords[0]][cur_coords[1]]

print(ceil(steps / 2))
