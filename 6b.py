from aoc import get_input
import re
import time

input = get_input(6).splitlines()
# input = [
#     'Time:      7  15   30',
#     'Distance:  9  40  200',
# ]

start_time = time.time()

def get_number_from_line(line):
    str_nums = re.findall(r'\s\d+', line.split(':')[1])
    total_str = ''
    for str_num in str_nums:
        total_str += str_num.lstrip()
    return int(total_str)

race_time = get_number_from_line(input[0])
distance = get_number_from_line(input[1])

solution_count = 0
for time_charging in range(1, race_time - 1):
    if (race_time - time_charging) * time_charging > distance:
        solution_count += 1

print(solution_count)
print("--- %s seconds ---" % (time.time() - start_time))
