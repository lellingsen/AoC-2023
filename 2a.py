from aoc import get_input

input = get_input(2).splitlines()

game_dict = {};

for line in input:
    number_and_games = line.split(':')
    game_number = int(number_and_games[0].split(' ')[1])
    games = number_and_games[1].split(';')
    game_dict[game_number] = {}
    for game in games:
        colors = game.split(',')
        for color in colors:
            # NOTE: could have exited early knowing the maxes ahead
            # of time, but that's unrealistic to the nature of the game...
            count_and_color = color.lstrip().split(' ')
            count = int(count_and_color[0])
            color = count_and_color[1]
            game_dict[game_number][color] = max(game_dict[game_number].get(color, 0), count)

max_values = {
    'red': 12,
    'green': 13,
    'blue': 14,
}
sum = 0

for game_number in game_dict:
    game_possible = True
    game_recap = game_dict[game_number]
    for color in max_values:
        if game_recap.get(color, 0) > max_values[color]:
            game_possible = False
            break

    if game_possible:
        sum += game_number

print(sum)
