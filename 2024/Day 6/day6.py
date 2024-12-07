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
    def simulate_guard(l, start_x, start_y, direction):
        x, y = start_x, start_y
        visited = set()
        while True:
            # Check if the guard is revisiting a state (position and direction)
            state = (x, y, direction)
            if state in visited:
                return True  # Guard is in a loop
            visited.add(state)

            # Next position
            nx = x + DX[direction]
            ny = y + DY[direction]

            if not is_coord_in(l, (nx,ny)):
                return False

            if l[nx, ny] == '#':
                direction = (direction + 1) % 4
            else:
                x, y = nx, ny

    possible_positions = 0
    k = 0
    direction = 0
    for i in range(len(l[0])):
        for j in range(len(l)):
            if l[i, j] == '.' and (i, j) != (start_x, start_y):
                l_copy = l.copy()
                l_copy[i, j] = '#'

                if simulate_guard(l_copy, start_x, start_y, direction):
                    possible_positions += 1
                else:
                    k+=1
    print(k)
    return possible_positions
                    
if __name__ == "__main__":
    l = read_file("input.txt")
    l = np.array([list(ligne) for ligne in l])
    result1 = part1(l)
    print(f"Résulat de la partie 1 : {result1[0]}")
    print(f"Résulat de la partie 2 : {part2(l, result1[1][0], result1[1][0])}")