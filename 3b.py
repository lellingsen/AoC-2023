import re
from aoc import get_input

input = get_input(3).splitlines()

parts_per_line = []
gears_per_line = []

for line in input:
    line_part_numbers = []
    line_symbols = []
    number_matches = re.finditer(r'\d+', line)
    for match in number_matches:
        part_number = match.group(0)
        line_part_numbers.append({ 
            'number': int(part_number), 
            'start': match.start(), 
            'end': match.end(),
        })

    parts_per_line.append(line_part_numbers)

    gear_matches = re.finditer(r'\*', line)
    for match in gear_matches:
        gear_match = {
            'symbol': match.group(0),
            'index': match.start(),
        }
        line_symbols.append(gear_match)

    gears_per_line.append(line_symbols)

sum = 0
for i, line_symbols in enumerate(gears_per_line):
    for gear in line_symbols:
        line_before = parts_per_line[i - 1] if i > 0 else []
        same_line = parts_per_line[i]
        line_after = parts_per_line[i + 1] if i < len(parts_per_line) - 1 else []
        possible_lines = [line_before, same_line, line_after]
        parts_adjacent_to_gear = []
        for line in possible_lines:
            for part in line:
                if part['start'] <= gear['index'] + 1 and part['end'] >= gear['index']:
                    parts_adjacent_to_gear.append(part)

        if len(parts_adjacent_to_gear) == 2:
            sum += parts_adjacent_to_gear[0]['number'] * parts_adjacent_to_gear[1]['number']

print(sum)
