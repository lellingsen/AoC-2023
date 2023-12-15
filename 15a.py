from aoc import get_input

input = get_input(15)
# input = 'rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'

def run_hash(str):
    value = 0

    for character in str:
        ascii_code = ord(character)
        value += ascii_code
        value *= 17
        value %= 256

    return value

steps = input.split(',')
sum = 0

for step in steps:
    value = run_hash(step)
    sum += value

print(sum)
