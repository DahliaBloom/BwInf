from argparse import ArgumentParser
from random import randrange
from copy import deepcopy
import json


def get_random_coord(arukone):
    y, x = randrange(n), randrange(n)
    has_starting_point = False

    for off in range(n * n):
        flat = (y * n + x + off) % (n * n)
        new_y, new_x = flat // n, flat % n
        if arukone[new_y][new_x] == 0:
            y, x = new_y, new_x
            has_starting_point = True
            break

    if has_starting_point:
        arukone[y][x] = id
        return y, x

    return None, None


def get_furthest_away(y, x, arukone):
    max_distance = 0
    max_x, max_y = None, None

    for i_y, row in enumerate(arukone):
        for i_x, field in enumerate(row):
            if field == 0:
                distance = abs(i_y - y) + abs(i_x - x)
                if distance > max_distance:
                    max_distance = distance
                    max_y, max_x = i_y, i_x

    return max_y, max_x


def possible_directions(y, x, arukone):
    directions = {'y-1', 'y+1', 'x-1', 'x+1'}

    if y == 0 or arukone[y - 1][x] != 0:
        directions.remove('y-1')
    if y + 1 == n or arukone[y + 1][x] != 0:
        directions.remove('y+1')

    if x == 0 or arukone[y][x - 1] != 0:
        directions.remove('x-1')
    if x + 1 == n or arukone[y][x + 1] != 0:
        directions.remove('x+1')

    return list(directions)


def update_coordinates(y, x, direction_to_go):
    if direction_to_go == 'y-1':
        y -= 1
    elif direction_to_go == 'y+1':
        y += 1
    elif direction_to_go == 'x-1':
        x -= 1
    elif direction_to_go == 'x+1':
        x += 1

    return y, x


if __name__ == '__main__':
    n = ArgumentParser().add_argument('-n', type=int, default=5).parse_args().n
    id = 1
    pairs = []
    paths = []

    arukone = [[0] * n for _ in range(n)]
    arukone_solved = deepcopy(arukone)

    while True:
        arukone_with_starting_points = deepcopy(arukone_solved)
        y, x = get_random_coord(arukone_with_starting_points)
        if y == None or not possible_directions(y, x, arukone_solved):
            break
        target_y, target_x = get_furthest_away(y, x, arukone_with_starting_points)
        if target_y == None:
            break

        arukone_current_id = deepcopy(arukone_solved)
        arukone_current_id[y][x] = id
        queue = [[(y, x)]]

        while True:
            line = queue.pop(0)
            y, x = line[-1]

            is_at_target = False
            for direction in possible_directions(y, x, arukone_current_id):
                new_y, new_x = update_coordinates(y, x, direction)
                arukone_current_id[new_y][new_x] = id
                new_line = deepcopy(line)
                new_line.append((new_y, new_x))
                queue.append(new_line)

                if (new_y, new_x) == (target_y, target_x):
                    is_at_target = True
                    break

            next_y, next_x = queue[0][-1]
            no_directions_left = len(queue) == 1 and not possible_directions(new_y, new_x, arukone_current_id)
            if no_directions_left or is_at_target:
                break

        line = queue.pop()
        pairs.append([[line[0][0], line[0][1]], [line[-1][0], line[-1][1]]])
        paths.append([])
        arukone[line[0][0]][line[0][1]] = id
        arukone[line[-1][0]][line[-1][1]] = id
        for y, x in line:
            paths[-1].append([y, x])
            arukone_solved[y][x] = id

        # if id > ceil(n / 2):
        #     break
        id += 1

    for row in arukone:
        print(" ".join(map(str, row)))
    print()
    for row in arukone_solved:
        print(" ".join(map(str, row)))

    # chunk-BKTIFNSO.js -> n
    json_out = {
        'n': n,
        'board': arukone_solved,
        'pairs': pairs,
        'paths': paths
    }
    print(json.dumps(json_out))
