import argparse

def read_file():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-f', '--file', type=str, default='input0.txt')
    file = arg_parser.parse_args().file
    
    with open(file, 'r') as f:
        lines = list(filter(lambda l: l != '', f.read().splitlines()))
    
    return [[0 for i in range(int(lines[1]))] for _ in range(int(lines[0]))], list(map(int, lines[2:]))


if __name__ == '__main__':
    bags, games = read_file()
    
    for i, game in enumerate(games):
        number_for_each_bag = game // len(bags)

        if (number_for_each_bag != 0):
            for bag in bags:
                bag[i] += number_for_each_bag

            games[i] -= number_for_each_bag  # faster than mod
    
    bag_position = 0
    for i, game in enumerate(games):
        for game_of_kind in range(game):
            bags[bag_position % len(bags)][i] += 1
            bag_position += 1

    print(bags)
