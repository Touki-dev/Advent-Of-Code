import numpy as np

def read_file(file):
    with open(file, 'r') as file:
        lignes = file.read().split('\n')
        return np.array([list(ligne) for ligne in lignes])

def find_routes(grid, start, end):
    dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    routes = []
    visited = {}
    queue = [(start, [start], 0, 0)]
    while queue:
        (y, x), history, curr_score, curr_dir = queue.pop(0)

        if (y, x) == end:
            routes.append((history, curr_score))
            continue
            
        if ((y, x), curr_dir) in visited and visited[((y, x), curr_dir)] < curr_score:
            continue

        visited[((y, x), curr_dir)] = curr_score

        for i, (dy, dx) in enumerate(dirs):
            if (curr_dir + 2) % 4 == i:
                continue

            ny, nx = y + dy, x + dx
            if grid[ny, nx] != "#" and (ny, nx) not in history:
                if i == curr_dir:
                    queue.append(((ny, nx), history + [(ny, nx)], curr_score + 1, i))  # move forward
                else:
                    queue.append(((y, x), history, curr_score + 1, i))  # turn

    return routes

def part1(l):
    walls = np.where(l == '#')
    start = (int(np.where(l == 'S')[0][0]), int(np.where(l == 'S')[1][0]))
    end = (int(np.where(l == 'E')[0][0]), int(np.where(l == 'E')[1][0]))
    
    new_walls = []
    for i in range(len(walls[0])):
        x, y = walls[0][i], walls[1][i]
        if 0 < x < len(l)-1 and 0 < y < len(l)-1:
            new_walls.append((int(x), int(y)))
    
    best_route_legit = min(find_routes(l, start, end), key=lambda route: route[1])[1]
    total += 1
    for coord in new_walls:
        l[coord] = "."
        routes = find_routes(l, start, end)
        best_route_cheat = min(routes, key=lambda route: route[1])[1]
        if best_route_legit - 100 >= best_route_cheat:
            ...
    
    return start, end

def part2(l):
    ...

if __name__ == "__main__":
    l = read_file("input.txt")
    print(f"Résulat de la partie 1 : {part1(l)}")
    print(f"Résulat de la partie 2 : {part2(l)}")