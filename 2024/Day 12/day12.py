import numpy as np
def read_file(file):
    with open(file, 'r') as f:
        lignes = f.read().split('\n')
        return np.array([list(ligne) for ligne in lignes if ligne])

DIRS = ((1,0),(0,1),(-1,0),(0,-1))

def findRegion(l, i, j):
    queue = [(i,j)]
    region = [(i,j)]
    while len(queue) > 0:
        for d in DIRS:
            next_coord = tuple(map(int, np.add(queue[0], d)))
            if 0 <= next_coord[0] < len(l) and 0 <= next_coord[1] < len(l[0]):
                if l[next_coord] == l[i,j] and next_coord not in region:
                    region.append(next_coord)
                    queue.append(next_coord)
        queue.pop(0)
    return region, l[i,j]

def part1(l):
    coord_parcelle = []
    for i in range(len(l)):
        for j in range(len(l[0])):
            region, letter = findRegion(l, i, j)
            if sorted(region) not in coord_parcelle:
                coord_parcelle.append(sorted(region))
    total = 0
    for t in coord_parcelle:
        p = 0
        for i in t:
            for d in DIRS:
                test_coord = tuple(map(int, np.add(i, d)))
                if 0 <= test_coord[0] < len(l) and 0 <= test_coord[1] < len(l[0]):
                    if l[test_coord] != l[i]:
                        p += 1
                else:
                    p += 1
        total += len(t) * p
    
    return total
    
def part2(l):
    ...

if __name__ == "__main__":
    l = read_file("input.txt")
    print(f"Résultat de la partie 1 : {part1(l)}")
    print(f"Résultat de la partie 2 : {part2(l)}")
