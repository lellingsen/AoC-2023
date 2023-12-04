from aoc import get_input

input = get_input(4).splitlines()

total_sum = 0

for line in input:
    winning_numbers = line[line.find(':') + 1:line.find(' | ')].lstrip().split(' ')
    winning_numbers = [num for num in winning_numbers if num != '']
    our_numbers = line[line.find('|') + 1:].lstrip().split(' ')
    our_numbers = [num for num in our_numbers if num != '']
    line_sum = 0
    for winner in winning_numbers:
        if winner in our_numbers:
            if line_sum == 0:
                line_sum = 1
            else:
                line_sum = line_sum * 2

    total_sum += line_sum

print(total_sum)
