from aoc import get_input

input = get_input(13).splitlines()
# input = [
#     '#.##..##.',
#     '..#.##.#.',
#     '##......#',
#     '##......#',
#     '..#.##.#.',
#     '..##..##.',
#     '#.#.##.#.',
#     '',
#     '#...##..#',
#     '#....#..#',
#     '..##..###',
#     '#####.##.',
#     '#####.##.',
#     '..##..###',
#     '#....#..#',
# ]

def calc_vertical_mirror_score(grid) -> int:
    mirrored_columns = [i for i in range(0, len(grid[0]) - 1)]
    for row in grid:
        new_mirrored_columns = mirrored_columns.copy()
        for i in mirrored_columns:
            is_mirrored = True
            left = i
            right = i + 1
            while left >= 0 and right < len(row):
                if row[left] != row[right]:
                    is_mirrored = False
                    break
                left -= 1
                right += 1
            if not is_mirrored:
                new_mirrored_columns.remove(i)
        mirrored_columns = new_mirrored_columns
    score = 0
    for col in mirrored_columns:
        score = max(score, col + 1)
    return score

def calc_horizontal_mirror_score(grid) -> int:
    mirrored_rows = [i for i in range(0, len(grid) - 1)]
    for i in range(0, len(grid)):
        is_mirrored = True
        top = i
        bottom = i + 1
        while top >= 0 and bottom < len(grid):
            if grid[top] != grid[bottom]:
                is_mirrored = False
                break
            top -= 1
            bottom += 1
        if not is_mirrored:
            mirrored_rows.remove(i)
    score = 0
    for row in mirrored_rows:
        score += (row + 1) * 100
    return score

def calc_mirror_score(grid) -> int:
    vert = calc_vertical_mirror_score(grid)
    horiz = calc_horizontal_mirror_score(grid)
    return vert + horiz

grid = []
sum = 0
for row in input:
    if row == '':
        sum += calc_mirror_score(grid)
        grid = []
        continue
    else:
        grid.append(row)

if grid:
    sum += calc_mirror_score(grid)
    
print(sum)
