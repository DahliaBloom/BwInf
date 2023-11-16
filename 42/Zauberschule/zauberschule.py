import argparse
from heapq import heappop, heappush
from icecream import ic


class Node:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.same_floor_neighbours = []
        self.other_floor_neighbour = []

    def distance_to(self, other_node):
        return abs(other_node.x - self.x) + abs(other_node.y - self.y) + 3 * abs(other_node.z - self.z)


def create_graph_from_file():
    parser = argparse.ArgumentParser()
    parser.add_argument('example_number', type=int, help='An integer between 0 and 5 representing the example to use')
    example_number = parser.parse_args().example_number

    if example_number < 0 or example_number > 5:
        print(
            f'./zauberschule{example_number}.txt does not represent any sample data from https://bwinf.de/bundeswettbewerb/42/1/')
        exit(1)

    with open(f'./zauberschule{example_number}.txt', 'r') as f:
        height, width = tuple(map(lambda x: int(x) - 2, f.readline().strip().split()))
        nodes = []

        for floor in range(2):
            f.readline()

            for y in range(height):
                for x, field in enumerate(f.readline().strip()[1:-1]):
                    if field == '#':
                        nodes.append(None)
                    else:
                        node = Node(x, y, floor)
                        if x > 0 and nodes[-1] is not None:
                            node.same_floor_neighbours.append(nodes[-1])
                            nodes[-1].same_floor_neighbours.append(node)
                        if y > 0 and nodes[-width] is not None:
                            node.same_floor_neighbours.append(nodes[-width])
                            nodes[-width].same_floor_neighbours.append(node)
                        if floor > 0 and nodes[-width * height] is not None:
                            node.other_floor_neighbour.append(nodes[-width * height])
                            nodes[-width * height].other_floor_neighbour.append(node)

                        nodes.append(node)

                        if field == 'A':
                            start_node = node
                        elif field == 'B':
                            target_node = node
            f.readline()
            f.readline()

        return start_node, target_node


if __name__ == '__main__':
    start_node, target_node = create_graph_from_file()

    predecessor_node = dict()
    boundary_heap = [(0, 0, (start_node, start_node))]
    counter = 1
    steps = 0

    while True:
        steps += 1
        distance_current_node, _, (parent_node, current_node) = heappop(boundary_heap)

        if current_node not in predecessor_node:
            predecessor_node[current_node] = parent_node

            if current_node == target_node:
                break

            for neighbours, weight in (
                    (current_node.same_floor_neighbours, 1), (current_node.other_floor_neighbour, 3)):
                for neighbour in neighbours:
                    if neighbour not in predecessor_node:
                        new_distance = distance_current_node + weight + target_node.distance_to(neighbour)
                        heappush(boundary_heap, (new_distance, counter, (current_node, neighbour)))
                        counter += 1

    trace = [target_node]
    while trace[-1] != start_node:
        trace.append(predecessor_node[trace[-1]])

    coord = list(map(lambda x: (x.x, x.y, x.z), trace))[::-1]
    ic(coord)
    ic(steps)
