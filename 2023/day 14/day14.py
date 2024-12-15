import numpy as np
from tqdm import tqdm

def read_file(file):
    with open(file, 'r') as file:
        lignes = file.read().split('\n')
        return np.array(list(map(list, lignes)))
    
def simulate_rolling(rock, l, d):
    x,y = rock
    nx = x
    
    if d[1] == 0:
        tj = l[rock[0]::d[0], rock[1]]
    else:
        tj = l[rock[0], rock[1]::d[1]]
    
    index_stop = np.where(tj == "#")
    
    if len(index_stop[0]) != 0
    for i in range(rock[0]):
        nx, ny = x + d[0], y + d[1]
        if 0 <= nx < len(l) and 0 <= ny < len(l[0]) and l[nx,ny] == ".":
            x, y = nx, ny
        else:
            return (x,y)
    return (x,y)

DIRS = ((-1,0),(0,1),(1,0),(0,-1))

def part1(l):
    rounded_rocks = [coord for coord in np.ndindex(l.shape) if l[coord] == "O"]
    for rock in rounded_rocks:
        new_pos = simulate_rolling(rock, l, (-1, 0))
        if new_pos:
            l[rock], l[new_pos] = ".", "O"
        
    rounded_rocks = [coord for coord in np.ndindex(l.shape) if l[coord] == "O"]
    total = 0
    for rock in rounded_rocks:
        total += len(l) - rock[0]
    return total

def part2(l):
    rounded_rocks = [tuple(coord) for coord in np.ndindex(l.shape) if l[coord] == "O"]
    for _ in tqdm(range(1000000000)):
        for d in DIRS:
            for rock in rounded_rocks:
                new_pos = simulate_rolling(rock, l, d)
                if new_pos:
                    l[rock], l[new_pos] = ".", "O"
        
    rounded_rocks = [coord for coord in np.ndindex(l.shape) if l[coord] == "O"]
    total = 0
    for rock in rounded_rocks:
        total += len(l) - rock[0]
    return total

if __name__ == "__main__":
    l = read_file("input.txt")
    print(f"Résulat de la partie 1 : {part1(l)}")
    with open("result.txt", "w") as fichier:
        fichier.write(str(part2(l)))