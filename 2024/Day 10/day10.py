import numpy as np

def read_file(file):
    with open(file, 'r') as f:
        lignes = f.read().split('\n')
        return np.array([list(map(int, list(ligne))) for ligne in lignes if ligne])

def findPath(l, coord):
    rows, cols = len(l), len(l[0])
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    arrivés = []
    queue = [coord]

    while queue:
        y, x = queue.pop(0)
        curr = l[y, x]
        _next = curr + 1
        for dy, dx in dirs:
            ny, nx = y + dy, x + dx
            if 0 <= ny < rows and 0 <= nx < cols and l[ny, nx] == _next:
                if _next == 9:
                    arrivés.append((ny, nx))
                else:
                    queue.append((ny, nx))
    return arrivés

def part1(l):
    coord_départ = [coord for coord in np.ndindex(l.shape) if l[coord] == 0]
    total = 0

    for coord in coord_départ:
        arrivés = findPath(l, coord)
        total += len(set(arrivés))
    
    return total

def part2(l):
    coord_départ = [coord for coord in np.ndindex(l.shape) if l[coord] == 0]
    total = 0

    for coord in coord_départ:
        cote = len(findPath(l, coord))
        total += cote
    
    return total

if __name__ == "__main__":
    l = read_file("input.txt")
    print(f"Résultat de la partie 1 : {part1(l)}")
    print(f"Résultat de la partie 2 : {part2(l)}")
