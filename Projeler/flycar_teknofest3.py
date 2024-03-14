class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0  # Gerçek maliyet (başlangıçtan bu düğüme olan mesafe)
        self.h = 0  # Heuristik maliyet (bu düğümden hedefe olan tahmini mesafe)
        self.f = 0  # Toplam maliyet (g + h)

def a_star(start, goal):
    open_list = []
    closed_list = []

    start_node = Node(start)
    goal_node = Node(goal)

    open_list.append(start_node)

    while open_list:
        current_node = min(open_list, key=lambda node: node.f)
        open_list.remove(current_node)
        closed_list.append(current_node)

        if current_node.position == goal_node.position:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]

        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Dört yöne hareket

        for neighbor in neighbors:
            new_position = (current_node.position[0] + neighbor[0], current_node.position[1] + neighbor[1])

            if new_position[0] < 0 or new_position[0] >= len(grid) or new_position[1] < 0 or new_position[1] >= len(grid[0]):
                continue

            if grid[new_position[0]][new_position[1]] == 1:
                continue

            neighbor_node = Node(new_position, current_node)
            neighbor_node.g = current_node.g + 1
            neighbor_node.h = abs(new_position[0] - goal_node.position[0]) + abs(new_position[1] - goal_node.position[1])
            neighbor_node.f = neighbor_node.g + neighbor_node.h

            if neighbor_node in closed_list:
                continue

            if neighbor_node not in open_list:
                open_list.append(neighbor_node)

    return None

# Örnek kullanım
grid = [[0, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]

start = (0, 0)
goal = (3, 3)

path = a_star(start, goal)
print("En kısa yol:", path)
