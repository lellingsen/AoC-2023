from aoc import get_input

input = get_input(9).splitlines()
# input = [
#     '0 3 6 9 12 15',
#     '1 3 6 10 15 21',
#     '10 13 16 21 30 45',
# ]

predicted_readings = []
for line in input:
    readings = [int(x) for x in line.split()]
    sequences = [readings]
    while True:
        differences = []
        for i in range(1, len(readings)):
            differences.append(readings[i] - readings[i-1])
        sequences.append(differences)
        if all([x == 0 for x in differences]):
            break
        readings = differences

    for i in range(len(sequences) - 1, -1, -1):
        sequence = sequences[i]
        prev_seq_val = 0
        if i < len(sequences) - 1:
            prev_seq_val = sequences[i+1][-1]
        sequence.append(sequence[-1] + prev_seq_val)

    predicted_readings.append(sequences[0][-1])

print(sum(predicted_readings))
