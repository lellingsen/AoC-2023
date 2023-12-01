from aoc import get_input
import re

data = get_input(1).splitlines()

number_dict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}
sum = 0

for line in data:
    # Use a lookahead because the words can overlap (like 'oneight')
    matches = re.finditer(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)
    digits = [match.group(1) for match in matches]
    first_num = digits[0]
    if number_dict.get(first_num) is not None:
        first_num = number_dict.get(first_num)
    last_num = digits[-1]
    if number_dict.get(last_num) is not None:
        last_num = number_dict.get(last_num)
    calib_value = str(first_num) + str(last_num)
    sum += int(calib_value)

print(sum)
