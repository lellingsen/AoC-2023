from aoc import get_input
import re

data = get_input(1).splitlines()

sum = 0
digit_regex = re.compile(r'\d')

for line in data:
    digits = digit_regex.findall(line)
    if digits is not None:
        first_num = digits[0]
        last_num = digits[-1]
        sum += int(first_num + last_num)

print(sum)
