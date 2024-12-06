import numpy as np
from tqdm import tqdm

def read_file(file):
    with open(file, 'r') as file:
        return file.read().split('\n')

def is_coord_in(l, coord):
    return 0 <= coord[0] < l.shape[0] and 0 <= coord[1] < l.shape[1]

def part1(l):
    coord_guard = []
    # Find guard
    for coord in np.ndindex(l.shape):
        if l[coord] == "^":
            coord_guard.append(coord)

    x,y = coord_guard[0]
    direction = 1
    j=0
    while 0<= x <=len(l[0]) and 0<= y <=len(l) and j<10000:
        if direction == 1:
            for i in range(len(l)):
                x-=1
                if not is_coord_in(l, (x,y)):
                    return len(set(coord_guard))
                if l[x,y] == "#":
                    x += 1
                    direction = 2
                    break
                coord_guard.append((x,y))
        if direction == 2:
            for i in range(len(l)):
                y+=1
                if not is_coord_in(l, (x,y)):
                    return len(set(coord_guard))
                if l[x,y] == "#":
                    y -= 1
                    direction = 3
                    break
                coord_guard.append((x,y))
        if direction == 3:
            for i in range(len(l)):
                x+=1
                if not is_coord_in(l, (x,y)):
                    return len(set(coord_guard))
                if l[x,y] == "#":
                    x -= 1
                    direction = 4
                    break
                coord_guard.append((x,y))
        if direction == 4:
            for i in range(len(l)):
                y-=1
                if not is_coord_in(l, (x,y)):
                    return len(set(coord_guard))
                if l[x,y] == "#":
                    y += 1
                    direction = 1
                    break
                coord_guard.append((x,y))
        j+=1
    return True
    
def part2(l):
    ...
    
if __name__ == "__main__":
    l = read_file("input.txt")
    l = np.array([list(ligne) for ligne in l])
    print(f"Résulat de la partie 1 : {part1(l)}")
    print(f"Résulat de la partie 1 : {part2(l)}")