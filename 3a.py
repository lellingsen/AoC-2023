import re
from aoc import get_input

input = get_input(3).splitlines()

parts_per_line = []
symbols_per_line = []

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
            'counted': False,
        })

    parts_per_line.append(line_part_numbers)

    symbol_matches = re.finditer(r'[^\d.]', line)
    for match in symbol_matches:
        symbol_match = {
            'symbol': match.group(0),
            'index': match.start(),
        }
        line_symbols.append(symbol_match)

    symbols_per_line.append(line_symbols)

sum = 0
for i, line_symbols in enumerate(symbols_per_line):
    for symbol in line_symbols:
        line_before = parts_per_line[i - 1] if i > 0 else []
        same_line = parts_per_line[i]
        line_after = parts_per_line[i + 1] if i < len(parts_per_line) - 1 else []
        possible_lines = [line_before, same_line, line_after]
        for line in possible_lines:
            for part in line:
                if not part['counted'] and part['start'] <= symbol['index'] + 1 and part['end'] >= symbol['index']:
                    part['counted'] = True
                    sum += part['number']

print(sum)
