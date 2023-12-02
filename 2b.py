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
            count_and_color = color.lstrip().split(' ')
            count = int(count_and_color[0])
            color = count_and_color[1]
            game_dict[game_number][color] = max(game_dict[game_number].get(color, 0), count)

sum = 0

for game_number in game_dict:
    game_power = 1
    game_recap = game_dict[game_number]
    for color in game_recap:
        game_power *= game_recap[color]

    sum += game_power

print(sum)
