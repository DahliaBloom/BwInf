import argparse
from random import randrange, choice
from math import ceil
from copy import deepcopy


def args():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-n', type=int, default=10)
    args_obj = arg_parser.parse_args()
    return args_obj.n


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

    if not directions:
        return None,

    return list(directions)


def update_coordinates(y, x, direction_to_go):
    match direction_to_go:
        case 'y-1':
            y -= 1
        case 'y+1':
            y += 1
        case 'x-1':
            x -= 1
        case 'x+1':
            x += 1

    return y, x


def choose_direction(y, x, target_y, target_x, arukone_solved, poss_directions):
    r_y, r_x = target_y - y, target_x - x

    if r_y == 0 == r_x:
        return None

    rules_set = ((r_y < 0, 'y-1'), (r_y > 0, 'y+1'), (r_x < 0, 'x-1'), (r_x > 0, 'x+1'))
    for rule in rules_set:
        if rule[0] and rule[1] in poss_directions:
            return rule[1]

    return choice(poss_directions)


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
        arukone[y][x] = -1
        return y, x
    
    return (None, None)


def grow(point, arukone_solved, arukone):
    (y, x), id, (target_y, target_x) = point

    poss_directions = possible_directions(y, x, arukone_solved)
    if poss_directions == (None,):
        arukone[y][x] = id
        return None

    direction_to_go = choose_direction(y, x, target_y, target_x, arukone_solved, poss_directions)

    if direction_to_go == None:
        arukone[y][x] = id
        return None

    y, x = update_coordinates(y, x, direction_to_go)
    arukone_solved[y][x] = id
    return [(y, x), id, (target_y, target_x)]


def pool_filter(start_point):
    (y, x), id, (target_y, target_x) = start_point
    if None in (y, x, target_y, target_x) or possible_directions(y, x, arukone_solved) == (None,):
        return False

    arukone[y][x] = id
    arukone_solved[y][x] = id
    return True
    

if __name__ == '__main__': 
    n = args()
    id_off = 1

    arukone = [[0 for _ in range(n)] for _ in range(n)]
    arukone_solved = deepcopy(arukone)
    
    while True:
        arukone_for_starting_points = deepcopy(arukone_solved)
        pool = [[get_random_coord(arukone_for_starting_points), i + id_off, get_random_coord(arukone_for_starting_points)] for i in range(ceil(n / 2))]
        pool = list(filter(pool_filter, pool))

        if not pool:
            break

        id_off += ceil(n / 2)
        
        while pool:
            pool = [out for line in pool if (out := grow(line, arukone_solved, arukone)) is not None]

    for row in arukone:
        print(" ".join(map(str, row)))
    print()
    for row in arukone_solved:
        print(" ".join(map(str, row)))
