MODE = 3
NUMBER = 3

def read_file(file):
    with open(file, 'r') as file:
        if MODE == 0:
            # return list of strings
            return [line.strip() for line in file]
        elif MODE == 1:
            # return list of tuples of strings
            return [tuple(line.strip().split()) for line in file]
        elif MODE == 2:
            # return list of integers
            return [int(line) for line in file]
        elif MODE == 3:
            # return list of digits in 2D list
            return [list(map(int, list(line.strip()))) for line in file]
        elif MODE == 4:
            # return list of tuples of integers
            return [tuple(map(int, line.strip().split())) for line in file]
        
def part1(grid):
    count = 0
    for y, line in enumerate(grid):
        for x, n in enumerate(line):
            visibility = [True, True, True, True]
            # top
            for i in range(y-1, -1, -1):
                if grid[i][x] >= n:
                    visibility[0] = False
                    break
            # bottom
            for i in range(y+1, len(grid)):
                if grid[i][x] >= n:
                    visibility[1] = False
                    break
            # left
            for i in range(x-1, -1, -1):
                if grid[y][i] >= n:
                    visibility[2] = False
                    break
            # right
            for i in range(x+1, len(line)):
                if grid[y][i] >= n:
                    visibility[3] = False
                    break
            
            if True in visibility:
                count += 1
    
    return count

def part2(grid):
    res = 0
    for y, line in enumerate(grid):
        for x, n in enumerate(line):
            visibility = [y, len(grid)-y, x, len(grid)-x]
            # top
            for i in range(y-1, -1, -1):
                visibility[0] = abs(y - i)
                if grid[i][x] >= n:
                    break
            # bottom
            for i in range(y+1, len(grid)):
                visibility[1] = abs(y - i)
                if grid[i][x] >= n:
                    break
            # left
            for i in range(x-1, -1, -1):
                visibility[2] = abs(x - i)
                if grid[y][i] >= n:
                    break
            # right
            for i in range(x+1, len(line)):
                visibility[3] = abs(x - i)
                if grid[y][i] >= n:
                    break
            
            produit = visibility[0] * visibility[1] * visibility[2] * visibility[3]
            if produit > res:
                res = produit
    
    return res

if __name__ == "__main__":
    l = read_file("input.txt")
    print(f"Résulat de la partie 1 : {part1(l)}")
    print(f"Résulat de la partie 2 : {part2(l)}")