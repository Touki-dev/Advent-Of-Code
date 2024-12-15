import re
import numpy as np

def read_file(file):
    with open(file, 'r') as file:
        lignes = file.read()
        resultat = re.findall(r"-?\d+,-?\d+", lignes)
        return [tuple(map(int, coord.split(','))) for coord in resultat]

def countRobot(c, l, h, grid):
    total = 1
    quadrants = ((0, 0, h//2, l//2), (h//2+1, 0, h, l//2), (0, l//2+1, h//2, l), (h//2+1, l//2+1, h, l))
    for i in range(4):
        start_y, start_x, end_y, end_x = quadrants[i]
        quadrant = grid[start_y:end_y:, start_x:end_x:]
        
        total *= np.sum(quadrant)
    return int(total)

def part1(robots, t):
    l = 101
    h = 103
    c = robots[::2]
    v = robots[1::2]
    
    for i in range(len(c)):
        px,py = c[i]
        vx,vy = v[i]
        c[i] = (px + vx*t) % l, (py + vy*t) % h
        
    grid = np.zeros((h, l))
    for coord in c:
        grid[coord[1], coord[0]] += 1
    grid = np.vectorize(int)(grid)
        
    return countRobot(c, l, h, grid), grid

def part2(l):
    for i in range(10000):
        if np.all(part1(l, i)[1] < 2):
            return i
    

if __name__ == "__main__":
    l = read_file("input.txt")
    print(f"Résulat de la partie 1 : {part1(l, 100)[0]}")
    print(f"Résulat de la partie 2 : {part2(l)}")
    
    # Affichage easter egg
    grid = np.vectorize(str)(part1(l, part2(l))[1])
    for i in range(len(grid)):
        print("".join(grid[i]))