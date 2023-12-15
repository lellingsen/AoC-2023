from aoc import get_input
import re

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
lens_regex = re.compile(r'[a-z]+')
operator_regex = re.compile(r'[-=\d]+')

boxes = {}

for step in steps:
    lens_label = lens_regex.search(step).group(0)
    operator = operator_regex.search(step).group(0)
    box_index = run_hash(lens_label)
    if operator == '-':
        if boxes.get(box_index) and lens_label in boxes[box_index]:
            del boxes[box_index][lens_label]
    elif operator[0] == '=':
        focal_length = operator[1]
        if box_index not in boxes:
            boxes[box_index] = {} 
        boxes[box_index][lens_label] = int(focal_length)

focusing_power = 0
for box_key in boxes.keys():
    for i, lens_label in enumerate(boxes[box_key].keys()):
        focusing_power += (box_key + 1) * (i + 1) * boxes[box_key][lens_label]

print(focusing_power)
