from aoc import get_input

input = get_input(12).splitlines()
# input = [
#     '???.### 1,1,3',
#     '.??..??...?##. 1,1,3',
#     '?#?#?#?#?#?#?#? 1,3,1,6',
#     '????.#...#... 4,1,1',
#     '????.######..#####. 1,6,5',
#     '?###???????? 3,2,1',
# ]


def get_combinations(string: str):
    combinations = []
    unknown_count = string.count('?')
    if unknown_count > 1:
        first_index = string.index('?')
        sub_combinations = get_combinations(string[first_index + 1:])
        beginning_of_str = string[:first_index + 1]
        for sub_combination in sub_combinations:
            combinations.append(beginning_of_str.replace('?', '.') + sub_combination)
            combinations.append(beginning_of_str.replace('?', '#') + sub_combination)
    else:
        combinations.append(string.replace('?', '.'))
        combinations.append(string.replace('?', '#'))
    return combinations

total_combos = 0
for row in input:
    row_combos = 0
    springs = row.split(' ')[0]
    groups = row.split(' ')[1].split(',')
    groups = [int(x) for x in groups]
    combinations = get_combinations(springs)
    for combo in combinations:
        combo_groups = [len(g) for g in combo.split('.') if g != '']
        if combo_groups == groups:
            row_combos += 1

    total_combos += row_combos

print(total_combos)
