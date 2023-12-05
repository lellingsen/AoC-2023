from aoc import get_input

input = get_input(5).splitlines()

seeds = input[0].split(': ')[1].split(' ')
tracker = {}
for seed in seeds:
    tracker[seed] = { 'current': int(seed), 'converted': False }

for line in input[2:]:
    if line == '':
        continue
    # if we're on a new map, reset the tracker
    if line.endswith('map:'):
        for key in tracker:
            tracker[key]['converted'] = False
        continue

    line_contents = line.split(' ')
    destination_range_start = int(line_contents[0])
    source_range_start = int(line_contents[1])
    range_length = int(line_contents[2])

    source_range_end = source_range_start + range_length - 1
    for key in tracker:
        cur_val = tracker[key]['current']
        if not tracker[key]['converted'] and cur_val >= source_range_start and cur_val <= source_range_end:
            tracker[key]['current'] = destination_range_start + (cur_val - source_range_start)
            tracker[key]['converted'] = True

min_location = None
for key in tracker:
    if min_location == None or tracker[key]['current'] < min_location:
        min_location = tracker[key]['current']

print(min_location)
