import argparse
from heapq import heappop, heappush

class Node:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def distance_to(self, other_node):
        return abs(other_node.x - self.x) + abs(other_node.y - self.y) + 3 * abs(other_node.z - self.z)

    @staticmethod
    def _get_neighbours(possible_neighbours):
        neighbours = []
        for neighbour_coords, has_neighbour in possible_neighbours:
            if has_neighbour:
                if neighbour_coords in nodes_pool:
                    neighbours.append(nodes_pool[neighbour_coords])
                else:
                    if floors[neighbour_coords[2]][neighbour_coords[1]][neighbour_coords[0]] != '#':
                        node = Node(neighbour_coords[0], neighbour_coords[1], neighbour_coords[2])
                        nodes_pool[neighbour_coords] = node
                        neighbours.append(node)

        return neighbours

    def same_floor_neighbours(self):
        return self._get_neighbours((
            ((self.x - 1, self.y, self.z), self.x > 0),
            ((self.x + 1, self.y, self.z), self.x < len(floors[0][0]) - 1),
            ((self.x, self.y - 1, self.z), self.y > 0),
            ((self.x, self.y + 1, self.z), self.y < len(floors[0]) - 1)))

    def other_floor_neighbour(self):
        return self._get_neighbours([((self.x, self.y, abs(self.z - 1)), True)])


def create_graph_from_file():
    parser = argparse.ArgumentParser()
    parser.add_argument('example_number', type=int, help='An integer between 0 and 5 representing the example to use')
    example_number = parser.parse_args().example_number

    if example_number < 0 or example_number > 5:
        print(
            f'./zauberschule{example_number}.txt does not represent any sample data from https://bwinf.de/bundeswettbewerb/42/1/')
        exit(1)

    with open(f'./zauberschule{example_number}.txt', 'r') as f:
        height, _ = map(int, f.readline().strip().split())
        fields = f.readlines()
        floors = []
        for floor in (fields[:height], fields[height + 1:2 * height + 1]):
            floor = floor[1:-1]
            floor = [list(row.strip()[1:-1]) for row in floor]
            floors.append(floor)

        for floor_number, floor in enumerate(floors):
            for y in range(len(floor)):
                for x in range(len(floor[0])):
                    if floor[y][x] in ('A', 'B'):
                        node = Node(x, y, floor_number)
                        nodes_pool[(x, y, floor_number)] = node
                        if floor[y][x] == 'A':
                            start_node = node
                        else:
                            target_node = node
                        if len(nodes_pool) == 2:
                            return start_node, target_node, floors

        raise Exception('Could not find start and target point')


if __name__ == '__main__':
    nodes_pool = dict()
    start_node, target_node, floors = create_graph_from_file()

    id = 0
    boundary_heap = [
        (0, id, (start_node, 0, start_node))]  # distance with heuristic, id, node, real distance, predecessor_node
    predecessor_nodes = dict()
    loaded_nodes = set()

    while True:
        if len(boundary_heap) == 0:
            raise Exception('No possible path from A to B found')
        _, _, (node, distance, predecessor_node) = heappop(boundary_heap)
        if node not in predecessor_nodes:
            predecessor_nodes[node] = predecessor_node
            loaded_nodes.add(node)
            if node == target_node:
                break
            for neighbours, neighbour_distance in (
                    (node.same_floor_neighbours(), 1), (node.other_floor_neighbour(), 3)):
                for neighbour in neighbours:
                    if neighbour not in predecessor_nodes:
                        alternative_distance = distance + neighbour_distance
                        distance_with_heuristic = alternative_distance + target_node.distance_to(neighbour)
                        id += 1
                        heappush(boundary_heap, (distance_with_heuristic, id, (neighbour, alternative_distance, node)))

    for node in loaded_nodes:
        floors[node.z][node.y][node.x] = '\033[33m.\033[0m' if floors[node.z][node.y][node.x] == '.' else '\033[32m' + \
                                                                                                          floors[
                                                                                                              node.z][
                                                                                                              node.y][
                                                                                                              node.x] + '\033[0m'

    time_required = 0
    trace = [target_node]
    while trace[-1] != start_node:
        from_node = predecessor_nodes[trace[-1]]
        to_node = trace[-1]
        time_required += 1

        if from_node != start_node:
            if from_node.x != to_node.x:
                floors[from_node.z][from_node.y][
                    from_node.x] = '\033[36m<\033[0m' if from_node.x > to_node.x else '\033[36m>\033[0m'
            elif from_node.y != to_node.y:
                floors[from_node.z][from_node.y][
                    from_node.x] = '\033[36m^\033[0m' if from_node.y > to_node.y else '\033[36mv\033[0m'
        if from_node.z != to_node.z:
            time_required += 2
            if to_node != target_node:
                floors[to_node.z][to_node.y][to_node.x] = '\033[31m!\033[0m'
            if from_node != start_node:
                floors[from_node.z][from_node.y][from_node.x] = '\033[31m!\033[0m'

        trace.append(from_node)

    for y in range(len(floors[0])):
        print(''.join(floors[0][y]) + '   ' + ''.join(floors[1][y]))

    print(f'\nTime required: \033[35m{time_required} seconds\033[0m')
