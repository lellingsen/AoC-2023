from aoc import get_input
import time

input = get_input(5).splitlines()
# input = [
#     'seeds: 79 14 55 13',
#     '',
#     'seed-to-soil map:',
#     '50 98 2',
#     '52 50 48',
#     '',
#     'soil-to-fertilizer map:',
#     '0 15 37',
#     '37 52 2',
#     '39 0 15',
#     '',
#     'fertilizer-to-water map:',
#     '49 53 8',
#     '0 11 42',
#     '42 0 7',
#     '57 7 4',
#     '',
#     'water-to-light map:',
#     '88 18 7',
#     '18 25 70',
#     '',  
#     'light-to-temperature map:',
#     '45 77 23',
#     '81 45 19',
#     '68 64 13',
#     '',
#     'temperature-to-humidity map:',
#     '0 69 1',
#     '1 0 69',
#     '',
#     'humidity-to-location map:',
#     '60 56 37',
#     '56 93 4',
# ]

start_time = time.time()

# how might we be able to speed this up?
# probably have to start working on everything as a range
# and then map the ranges all the way down
# split them as needed when only partially covered
# and then we'd have a final group of ranges and could get the minimum location
# so that would look like....
# get the range for each seed
# loop over the mappings, creating sub-ranges for ones that don't fully overlap
# do that all the way down until we get to locations
# add those locations to an array (or even just the minimum one from the whole group)
# continue for each seed range

seed_info = input[0].split(': ')[1].split(' ')

conversion_map = []
for line in input[2:]:
    if line == '':
        continue
    if line.endswith('map:'):
        conversion_map.append([])
        continue

    line_contents = line.split(' ')
    dest_start = int(line_contents[0])
    source_start = int(line_contents[1])
    range_length = int(line_contents[2])
    conversion_map[-1].append({
        'dest_start': dest_start,
        'source_start': source_start,
        'range_length': range_length,
    })

min_location = None
for i in range(0, len(seed_info), 2):
    range_start = int(seed_info[i])
    range_len = int(seed_info[i + 1])
    for seed in range(range_start, range_start + range_len):
        for category in conversion_map:
            for mapping in category:
                if seed >= mapping['source_start'] and seed <= mapping['source_start'] + mapping['range_length'] - 1:
                    seed = mapping['dest_start'] + (seed - mapping['source_start'])
                    break
        if min_location == None or seed < min_location:
            min_location = seed

print(min_location)
print("--- %s seconds ---" % (time.time() - start_time))
