import sys
from typing import Tuple
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

energy_grid = []
for line in input:
    energy_grid.append(['.'] * len(line))


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


def track_beam(direction: BeamDirection, x: int, y: int) -> None:
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
    track_beam(newDirection, newCoords[0], newCoords[1])
    if secondDirection != BeamDirection.NONE:
        secondCoords = get_next_coords(secondDirection, x, y)
        track_beam(secondDirection, secondCoords[0], secondCoords[1])

track_beam(BeamDirection.RIGHT, 0, 0)

cells_energized = 0
for row in energy_grid:
    cells_energized += row.count('#')

print(cells_energized)
