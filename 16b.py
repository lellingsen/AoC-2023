import sys
from typing import Tuple, List
from aoc import get_input
from enum import Enum

input = get_input(16).splitlines()
sys.setrecursionlimit(10000)
# input = [
#     '.|...\\....',
#     '|.-.\\.....',
#     '.....|-...',
#     '........|.',
#     '..........',
#     '.........\\',
#     '..../.\\\\..',
#     '.-.-/..|..',
#     '.|....-|.\\',
#     '..//.|....',
# ]

class BeamDirection(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4
    NONE = 5

def create_energy_grid() -> List[List[str]]:
    energy_grid = []
    for line in input:
        energy_grid.append(['.'] * len(line))
    return energy_grid


# Could end up in a circular loop
beams_tracked = []

def get_next_coords(direction: BeamDirection, x: int, y: int) -> Tuple[int, int]:
    new_x = x
    new_y = y
    if direction == BeamDirection.RIGHT:
        new_x += 1
    elif direction == BeamDirection.LEFT:
        new_x -= 1
    elif direction == BeamDirection.DOWN:
        new_y += 1
    else:
        new_y -= 1

    return (new_x, new_y)


def track_beam(direction: BeamDirection, x: int, y: int, energy_grid: List[List[str]]) -> None:
    if x < 0 or y < 0 or x >= len(input[0]) or y >= len(input):
        return

    beam_key = (direction, x, y)
    if beam_key in beams_tracked:
        return

    energy_grid[y][x] = '#'
    beams_tracked.append(beam_key)

    newDirection = BeamDirection.NONE
    secondDirection = BeamDirection.NONE
    cell = input[y][x]
    if cell == '.':
        newDirection = direction
    elif cell == '|':
        if (direction == BeamDirection.DOWN or direction == BeamDirection.UP):
            newDirection = direction
        else:
            newDirection = BeamDirection.DOWN
            secondDirection = BeamDirection.UP
    elif cell == '-':
        if (direction == BeamDirection.LEFT or direction == BeamDirection.RIGHT):
            newDirection = direction
        else:
            newDirection = BeamDirection.RIGHT
            secondDirection = BeamDirection.LEFT
    elif cell == '/':
        if direction == BeamDirection.UP:
            newDirection = BeamDirection.RIGHT
        elif direction == BeamDirection.DOWN:
            newDirection = BeamDirection.LEFT
        elif direction == BeamDirection.LEFT:
            newDirection = BeamDirection.DOWN
        else:
            newDirection = BeamDirection.UP
    elif cell == '\\':
        if direction == BeamDirection.UP:
            newDirection = BeamDirection.LEFT
        elif direction == BeamDirection.DOWN:
            newDirection = BeamDirection.RIGHT
        elif direction == BeamDirection.LEFT:
            newDirection = BeamDirection.UP
        else:
            newDirection = BeamDirection.DOWN

    newCoords = get_next_coords(newDirection, x, y)
    track_beam(newDirection, newCoords[0], newCoords[1], energy_grid)
    if secondDirection != BeamDirection.NONE:
        secondCoords = get_next_coords(secondDirection, x, y)
        track_beam(secondDirection, secondCoords[0], secondCoords[1], energy_grid)


def count_cells_energized(energy_grid: List[List[str]]) -> int:
    cells_energized = 0
    for row in energy_grid:
        cells_energized += row.count('#')
    return cells_energized

# grid = create_energy_grid()
# track_beam(BeamDirection.DOWN, 3, 0, grid)
# print(grid)
# print(count_cells_energized(grid))

max_cells_energized = 0
for y in range(len(input)):
    beams_tracked = []
    temp_grid = create_energy_grid()
    track_beam(BeamDirection.RIGHT, 0, y, temp_grid)
    energized = count_cells_energized(temp_grid)
    max_cells_energized = max(max_cells_energized, energized)

    beams_tracked = []
    temp_grid = create_energy_grid()
    track_beam(BeamDirection.LEFT, len(input[y]) - 1, y, temp_grid)
    energized = count_cells_energized(temp_grid)
    max_cells_energized = max(max_cells_energized, energized)

for x in range(len(input[0])):
    beams_tracked = []
    temp_grid = create_energy_grid()
    track_beam(BeamDirection.DOWN, x, 0, temp_grid)
    energized = count_cells_energized(temp_grid)
    max_cells_energized = max(max_cells_energized, energized)

    beams_tracked = []
    temp_grid2 = create_energy_grid()
    track_beam(BeamDirection.UP, x, len(input) - 1, temp_grid2)
    energized = count_cells_energized(temp_grid2)
    max_cells_energized = max(max_cells_energized, energized)


print(max_cells_energized)
