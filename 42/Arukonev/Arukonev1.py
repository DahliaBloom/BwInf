import argparse
from random import randrange, choice


def args():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("-n", type=int, default=4)
    return arg_parser.parse_args()


def possible_directions(y, x, arukone):
    n = len(arukone)
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
    if direction_to_go == 'y-1':
        y -= 1
    elif direction_to_go == 'y+1':
        y += 1
    elif direction_to_go == 'x-1':
        x -= 1
    elif direction_to_go == 'x+1':
        x += 1

    return y, x


def create_line(y, x, arukone_solved, id):
    added_segments = 0
    last_direction = None

    while True:
        arukone_solved[y][x] = id
        added_segments += 1

        poss_directions = possible_directions(y, x, arukone_solved)
        if poss_directions == (None,) or added_segments > len(arukone_solved) ** 1.5:
            return y, x
        
        if last_direction in poss_directions:
            direction_to_go = last_direction
        else:
            direction_to_go = choice(poss_directions)

        last_direction = direction_to_go
        y, x = update_coordinates(y, x, direction_to_go)
    

if __name__ == '__main__': 
    n = args().n
    id = 1

    arukone = [[0 for _ in range(n)] for _ in range(n)]
    arukone_solved = [[0 for _ in range(n)] for _ in range(n)]

    while True:
        y, x = randrange(n), randrange(n)
        has_starting_point = False

        for off in range(n * n):
            print(off)
            flat = (y * n + x + off) % (n * n)
            new_y, new_x = flat // n, flat % n
            if possible_directions(new_y, new_x, arukone_solved) != (None,):
                y, x = new_y, new_x
                has_starting_point = True
                break

        if not has_starting_point:
            break

        while True:
            direction_to_go = choice(possible_directions(y, x, arukone_solved))
            if direction_to_go == None:
                break

            y, x = update_coordinates(y, x, direction_to_go)
            if possible_directions(y, x, arukone_solved) == (None,):
                break

            arukone[y][x] = id

            y, x = create_line(y, x, arukone_solved, id)
            arukone[y][x] = id

            id += 1

    for row in arukone:
        print(" ".join(map(str, row)))
    print()
    for row in arukone_solved:
        print(" ".join(map(str, row)))
