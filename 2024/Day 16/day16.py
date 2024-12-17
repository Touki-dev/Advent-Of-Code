import numpy as np

def read_file(file):
    with open(file, 'r') as file:
        lignes = file.read().split('\n')
        return np.array(list(map(list, lignes)))

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
                if grid[ny][nx] != "#" and (ny, nx) not in history:
                    if i == curr_dir:
                        queue.append(((ny, nx), history + [(ny, nx)], curr_score + 1, i))  # move forward
                    else:
                        queue.append(((y, x), history, curr_score + 1000, i))  # turn

        return routes

def printGrid(grid):
    for i in grid:
        print("".join(i))
        
def part1(grid):
    start = (len(grid)-2, 1)
    end = (1, len(grid)-2)
    
    routes = find_routes(grid, start, end)
    return min(r[1] for r in routes)

def part2(grid):
    start = (len(grid)-2, 1)
    end = (1, len(grid)-2)
    
    routes = find_routes(grid, start, end)
    min_score = min(r[1] for r in routes)
    tiles = []
    while True:
        route = min(routes, key=lambda route: route[1])
        if route[1] == min_score:
            print(route)
            for j in route[0]:
                tiles.append(j)
        else:
            break
        routes.remove(route)
        
    return len(set(tiles))

if __name__ == "__main__":
    l = read_file("input.txt")
    print(f"Résulat de la partie 1 : {part1(l)}")
    print(f"Résulat de la partie 2 : {part2(l)}")