from aoc import get_input
from functools import cache

input = get_input(12).splitlines()
# input = [
#     '???.### 1,1,3',
#     '.??..??...?##. 1,1,3',
#     '?#?#?#?#?#?#?#? 1,3,1,6',
#     '????.#...#... 4,1,1',
#     '????.######..#####. 1,6,5',
#     '?###???????? 3,2,1',
# ]

# Help from https://github.com/xavdid/advent-of-code/blob/main/solutions/2023/day_12/solution.py
@cache
def get_arrangements(row: str, groups: tuple[int]) -> int:
    # if we're out of groups, done if there are no more springs
    if not groups:
        # '?' could just be ground ('.')
        return '#' not in row
    # if we're at end, row is done if groups are done
    if not row:
        return len(groups) == 0

    cell, rest_of_row = row[0], row[1:]

    if cell == '.':
        return get_arrangements(rest_of_row, groups)

    if cell == '#':
        group = groups[0]
        long_enough = len(row) >= group
        all_maybe_springs = all(x != '.' for x in row[:group])
        group_terminates = long_enough and (len(row) == group or row[group] != '#')
        if long_enough and all_maybe_springs and group_terminates:
            return get_arrangements(row[group + 1:], groups[1:])
        else:
            return 0
    
    # we're in the "?" state
    if_spring = get_arrangements('#' + rest_of_row, groups)
    if_ground = get_arrangements('.' + rest_of_row, groups)
    return if_spring + if_ground

def arrangements_for_row(row: str) -> int:
    springs = row.split(' ')[0]
    springs = '?'.join([springs] * 5)
    groups = row.split(' ')[1]
    groups = ','.join([groups] * 5)
    groups = groups.split(',')
    groups = tuple([int(x) for x in groups])
    return get_arrangements(springs, groups)


total_combos = 0
for row in input:
    row_combos = arrangements_for_row(row)
    total_combos += row_combos

print(total_combos)
