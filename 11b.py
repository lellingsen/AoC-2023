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

empty_rows = []
empty_columns = []
col_length = len(input[0])
for i, row in enumerate(input):
    if row.find('#') == -1:
        empty_rows.append(i)

for j, column in enumerate(zip(*input)):
    if ''.join(column).find('#') == -1:
        empty_columns.append(j)

galaxies = []
for i, row in enumerate(input):
    for j, char in enumerate(row):
        if char == '#':
            galaxies.append((i, j))

min_distances = []
for i, galaxy in enumerate(galaxies):
    for j in (range(i + 1, len(galaxies))):
        other_galaxy = galaxies[j]
        # need to see how many empty rows and columns we're passing through
        # then add a million for each one
        empty_rows_passed_through = [empty_row for empty_row in empty_rows if empty_row > galaxy[0] and empty_row < other_galaxy[0]]
        first_col = min(galaxy[1], other_galaxy[1])
        second_col = max(galaxy[1], other_galaxy[1])
        empty_cols_passed_through = [empty_col for empty_col in empty_columns if empty_col > first_col and empty_col < second_col]
        distance = abs(galaxy[0] - other_galaxy[0]) + abs(galaxy[1] - other_galaxy[1])
        distance += len(empty_rows_passed_through) * (1000000 - 1)
        distance += len(empty_cols_passed_through) * (1000000 - 1)
        min_distances.append(distance)

print(sum(min_distances))

