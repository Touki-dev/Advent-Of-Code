import numpy as np

FORMAT = 1

def read_file(file):
    with open(file, 'r') as f:
        lignes = f.read().split('\n')
        if FORMAT == 1:  # Grid
            return np.array([list(map(int, list(ligne))) for ligne in lignes if ligne])

def findChemin(l, coord):
    dir_x = [0, 1, 0, -1]
    dir_y = [-1, 0, 1, 0]
    n_arrivé = set()
    queue = [coord]
    
    while queue:
        n_direction = []
        coord = queue.pop(0)
        for dir in range(4):
            new_coord = (coord[0] + dir_y[dir], coord[1] + dir_x[dir])
            if (0 <= new_coord[0] < l.shape[0]) and (0 <= new_coord[1] < l.shape[1]):
                if l[coord]+1 == l[new_coord]:
                    n_direction.append(new_coord)
        
        if len(n_direction) > 1:
            for i in range(1, len(n_direction)):
                queue.append(n_direction[i])
        if len(n_direction) == 1:
            if l[n_direction[0]] == 9:
                n_arrivé.add(n_direction[0])
            else:
                queue.append(n_direction[0])
        if len(n_direction) == 0:
            n_arrivé.add(coord)
    
    return n_arrivé

def part1(l):
    coord_départ = [coord for coord in np.ndindex(l.shape) if l[coord] == 0]
    total = 0
    for coord in coord_départ:
        total += len(findChemin(l, coord))
    return total

if __name__ == "__main__":
    l = read_file("input.txt")
    print(f"Résultat de la partie 1 : {part1(l)}")
