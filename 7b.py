from aoc import get_input
import time

input = get_input(7).splitlines()
# input = [
#     '32T3K 765',
#     'T55J5 684',
#     'KK677 28',
#     'KTJJT 220',
#     'QQQJA 483',
# ]

card_strengths = {
    'A': 'a', 
    'K': 'b', 
    'Q': 'c', 
    'J': 'n', 
    'T': 'e', 
    '9': 'f', 
    '8': 'g', 
    '7': 'h', 
    '6': 'i', 
    '5': 'j', 
    '4': 'k', 
    '3': 'l', 
    '2': 'm',
}

hands = []
for line in input:
    hand, bid = line.split(' ')
    bid = int(bid)
    card_counts = {}
    for card in hand:
        card_counts[card] = card_counts.get(card, 0) + 1

    joker_count = card_counts.get('J', 0)
    if joker_count > 0:
        card_counts['J'] = 0
        max_card = max(card_counts, key=card_counts.get) 
        card_counts[max_card] += joker_count

    pair_count = sum(value == 2 for value in card_counts.values())
    hand_strength = 1
    if 5 in card_counts.values():
        hand_strength = 7
    elif 4 in card_counts.values():
        hand_strength = 6
    elif 3 in card_counts.values():
        if 2 in card_counts.values():
            hand_strength = 5
        else:
            hand_strength = 4
    elif pair_count == 2:
        hand_strength = 3
    elif pair_count == 1:
        hand_strength = 2

    hand_card_strengths = ''.join(card_strengths[card] for card in hand)

    hands.append({ 
        'hand': hand, 
        'bid': bid, 
        'hand_strength': hand_strength,
        'card_strengths': hand_card_strengths
    })

hands.sort(key=lambda hand: (-hand['hand_strength'],hand['card_strengths']))

winnings = 0
for i, hand in enumerate(hands):
    winnings += hand['bid'] * (len(hands) - i)

print(winnings)
