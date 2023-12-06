from aoc import get_input
import re
import time

input = get_input(6).splitlines()
# input = [
#     'Time:      7  15   30',
#     'Distance:  9  40  200',
# ]

start_time = time.time()


def get_numbers_from_line(line):
    str_nums = re.findall(r'\s\d+', line.split(':')[1])
    nums = []
    for str_num in str_nums:
        nums.append(int(str_num.lstrip()))
    return nums

times = get_numbers_from_line(input[0])
distances = get_numbers_from_line(input[1])

possible_ways = []
for i in range(0, len(times)):
    race_time = times[i]
    distance = distances[i]
    solution_count = 0
    for time_charging in range(1, race_time - 1):
        if (race_time - time_charging) * time_charging > distance:
            solution_count += 1
    possible_ways.append(solution_count)

total_ways = 1
for way in possible_ways:
    total_ways *= way

print(total_ways)
print("--- %s seconds ---" % (time.time() - start_time))
