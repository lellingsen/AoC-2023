from aoc import get_input

input = get_input(4).splitlines()

copies = {}

for i in range(0, len(input)):
    copies[i + 1] = 1

for i, line in enumerate(input):
    copies_for_this_line = copies.get(i + 1, 1)
    winning_numbers = line[line.find(':') + 1:line.find(' | ')].lstrip().split(' ')
    winning_numbers = [num for num in winning_numbers if num != '']
    our_numbers = line[line.find('|') + 1:].lstrip().split(' ')
    our_numbers = [num for num in our_numbers if num != '']
    line_sum = 0
    for winner in winning_numbers:
        if winner in our_numbers:
            line_sum += 1

    for j in range(1, line_sum + 1):
        copies[i + j + 1] += copies_for_this_line

print(sum(copies.values()))
