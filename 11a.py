from aoc import get_input

input = get_input(11).splitlines()
# input = [
#     '...#......',
#     '.......#..',
#     '#.........',
#     '..........',
#     '......#...',
#     '.#........',
#     '.........#',
#     '..........',
#     '.......#..',
#     '#...#.....',
# ]

# account for space expanding
empty_rows = []
empty_columns = []
col_length = len(input[0])
for i, row in enumerate(input):
    if row.find('#') == -1:
        empty_rows.append(i)

for j, column in enumerate(zip(*input)):
    if ''.join(column).find('#') == -1:
        empty_columns.append(j)

for i in range(len(empty_rows) - 1, -1, -1):
    input.insert(empty_rows[i], '.' * col_length)

for j in range(len(empty_columns) - 1, -1, -1):
    col_to_insert = empty_columns[j]
    for i in range(len(input)):
        input[i] = input[i][:col_to_insert] + '.' + input[i][col_to_insert:]

galaxies = []
for i, row in enumerate(input):
    for j, char in enumerate(row):
        if char == '#':
            galaxies.append((i, j))

min_distances = []
for i, galaxy in enumerate(galaxies):
    for j in (range(i + 1, len(galaxies))):
        distance = abs(galaxy[0] - galaxies[j][0]) + abs(galaxy[1] - galaxies[j][1])
        min_distances.append(distance)

print(sum(min_distances))

