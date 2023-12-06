from aoc import get_input
import time

input = get_input(5).splitlines()

start_time = time.time()

# Needed to speed up the original solution
# Had to work on ranges instead of individual values
# The hard part was when ranges had to split, and handling which parts of
# the range had already been mapped

seed_info = input[0].split(': ')[1].split(' ')

conversion_map = []
current_mappings = []

# Order the mappings by source value so that
# we can more easily know if we already handled the beginning/end
# of a range later
for line in input[2:]:
    if line == '':
        continue
    if line.endswith('map:'):
        current_mappings = sorted(current_mappings, key=lambda x: x['source'])
        if len(current_mappings) > 0:
            conversion_map.append(current_mappings)
        current_mappings = []
        continue

    line_contents = line.split(' ')
    dest_start = int(line_contents[0])
    source_start = int(line_contents[1])
    range_length = int(line_contents[2])
    current_mappings.append({
        'dest': dest_start,
        'source': source_start,
        'len': range_length,
    })

current_mappings = sorted(current_mappings, key=lambda x: x['source'])
conversion_map.append(current_mappings)

min_location = None
for i in range(0, len(seed_info), 2):
    range_start = int(seed_info[i])
    range_len = int(seed_info[i + 1])
    ranges = [{ 'start': range_start, 'len': range_len }]
    for category in conversion_map:
        new_ranges = []
        for cur_range in ranges:
            mappings_for_range = []
            last_value_mapped = None
            # mappings are ordered
            first_mapping = True
            for mapping in category:
                # check for any overlap
                range_end = cur_range['start'] + cur_range['len'] - 1
                mapping_end = mapping['source'] + mapping['len'] - 1
                if cur_range['start'] <= mapping_end and mapping['source'] <= range_end:
                    offset = cur_range['start'] - mapping['source']
                    # Add the mapped part of the range
                    new_range_start = mapping['dest'] + max(offset, 0)
                    new_range_end = min(range_end, mapping_end)
                    new_range_len = new_range_end - max(cur_range['start'], mapping['source']) + 1
                    mapped_range = { 'start': new_range_start, 'len': new_range_len }
                    mappings_for_range.append(mapped_range)
                    first_value_mapped = mapping['source'] + max(offset, 0) - 1
                    last_value_mapped = max(first_value_mapped + new_range_len, last_value_mapped if last_value_mapped is not None else 0)
                    # If we didn't cover the start of the range, need to add that in unmapped
                    if first_mapping and offset < 0:
                        beginning_of_range = { 'start': cur_range['start'], 'len': abs(offset) }
                        mappings_for_range.append(beginning_of_range)
                first_mapping = False
            # did any mappings match? if not, add the whole range (unmapped)
            if len(mappings_for_range) == 0:
                mappings_for_range.append(cur_range)
            # did we cover the end of the range? if not, add it
            range_end = cur_range['start'] + cur_range['len'] - 1
            if last_value_mapped is not None and last_value_mapped < range_end:
                end_of_range = { 'start': last_value_mapped + 1, 'len': range_end - last_value_mapped }
                mappings_for_range.append(end_of_range)

            new_ranges += mappings_for_range
        ranges = new_ranges

    min_range_start = sorted(ranges, key=lambda x: x['start'])[0]['start']
    if min_location is None or min_range_start < min_location:
        min_location = min_range_start 

print(min_location)
print("--- %s seconds ---" % (time.time() - start_time))
