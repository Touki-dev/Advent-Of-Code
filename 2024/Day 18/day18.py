import numpy as np

def read_file(file):
    with open(file, 'r') as file:
        lignes = file.read().split('\n')
        return [tuple(map(int, ligne.split(","))) for ligne in lignes]

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
                    queue.append(((y, x), history, curr_score + 1, i))  # turn

    return routes

def printGrid(grid):
    for i in grid:
        print("".join(i))

def part1(l):
    x_max = max(l, key=lambda x: x[0])
    y_max = max(l, key=lambda y: y[1])
    
    grid = np.full((y_max[1]+3, x_max[0]+3), ".")
    grid[::len(grid)-1, ::] = "#"
    grid[::, ::len(grid[0])-1] = "#"
    
    start = (1,1)
    end = (y_max[1]+1, x_max[0]+1)
    grid[end] = "%"
    
    for i in range(1024):
        grid[l[i][0]+1, l[i][1]+1] = "#"
    
    routes = find_routes(grid, start, end)
    best_route = min(routes, key=lambda route: route[1])
        
    return len(best_route[0])-3, best_route[0]
    
def part2(l):
    x_max = max(l, key=lambda x: x[0])
    y_max = max(l, key=lambda y: y[1])
    
    grid = np.full((y_max[1]+3, x_max[0]+3), ".")
    grid[::len(grid)-1, ::] = "#"
    grid[::, ::len(grid[0])-1] = "#"
    
    start = (1,1)
    end = (y_max[1]+1, x_max[0]+1)
    grid[end] = "%"
    
    best_route = part1(l)[1]
    for i in range(len(l)):
        grid[l[i][0]+1, l[i][1]+1] = "#"
        if i > 1024 and (l[i][0]+1, l[i][1]+1) in best_route:
            test = find_routes(grid, start, end)
            if not test:
                return l[i]
            else:
                best_route = min(test, key=lambda route: route[1])[0]
                print(i)

if __name__ == "__main__":
    l = read_file("input.txt")
    print(f"Résulat de la partie 1 : {part1(l)[0]}")
    print(f"Résulat de la partie 2 : {part2(l)}")