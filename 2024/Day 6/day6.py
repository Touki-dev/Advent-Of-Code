import numpy as np
from tqdm import tqdm

def read_file(file):
    with open(file, 'r') as file:
        return file.read().split('\n')

def is_coord_in(l, coord):
    return 0 <= coord[0] < l.shape[0] and 0 <= coord[1] < l.shape[1]

DX = [-1, 0, 1, 0]  # Change in row for each direction
DY = [0, 1, 0, -1]  # Change in column for each direction
    
def part1(l):
    # Find guard
    coord_guard = [coord for coord in np.ndindex(l.shape) if l[coord] == "^"]
    
    x,y = coord_guard[0]
    direction = 0
    
    while 0<= x <=len(l[0]) and 0<= y <=len(l):
        for i in range(len(l)):
            nx,ny = x,y
            nx = x + DX[direction]
            ny = y + DY[direction]
            if not is_coord_in(l, (nx,ny)):
                return len(set(coord_guard)), coord_guard[0]
            if l[nx,ny] == "#":
                direction = (direction + 1) % 4
                break
            else:
                x,y = nx,ny
            coord_guard.append((x,y))
    
def part2(l, start_x, start_y):
    ...
                    
if __name__ == "__main__":
    l = read_file("input.txt")
    l = np.array([list(ligne) for ligne in l])
    result1 = part1(l)
    print(f"Résulat de la partie 1 : {result1[0]}")