from tqdm import tqdm

def read_file(file):
    with open(file, 'r') as file:
        lignes = file.read().split('\n')
        return [list(ligne) for ligne in lignes]

DIRS = { (0, -1): "<", (0, 1): ">", (-1, 0): "^", (1, 0): "v" }


def process(digicode, keypad):
    k = {}
    for i in range(len(keypad)):
        for j in range(len(keypad[i])):
            k[keypad[i][j]] = (i,j)
            
    pos = k["A"]
    queue = [([], pos, 0)]
    paths = []
    while queue:
        history, (y,x), key = queue.pop(0)
        target = k[digicode[key]]
        dist = (abs(y - target[0]), abs(x - target[1]))
        i=0
        if target == (y,x):
            if key+1 == len(digicode):
                paths.append(history + ["A"])
            else:
                queue.append((history + ["A"], (y,x), key+1))
        else:
            for d in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                ny,nx = y+d[0], x+d[1]
                ndist = (abs(ny - target[0]), abs(nx - target[1]))
                if (ny,nx) == target:
                    if key+1 == len(digicode):
                        paths.append(history + [DIRS[d], "A"])
                    else:
                        queue.append((history + [DIRS[d], "A"], (ny,nx), key+1))
                elif sum(ndist) < sum(dist) and (ny,nx) != k["N"]:
                    queue.append((history + [DIRS[d]], (ny,nx), key))
    return paths

def part1(l):
    keypad1 = [
        ["7", "8", "9"],
        ["4", "5", "6"],
        ["1", "2", "3"],
        ["N", "0", "A"]
    ]
    keypad2 = [
        ["N", "^", "A"],
        ["<", "v", ">"]
    ]
    
    total=0
    for digicode in tqdm(l):
        all_paths = []
        for path in tqdm(process(digicode, keypad1)):
            for path2 in process(path, keypad2):
                all_paths.append(min(process(path2, keypad2), key=len))
        m = min(all_paths, key=len)
        total += len(m) * int("".join(digicode)[:3])
                
    return total

def part2(l):
    ...

if __name__ == "__main__":
    l = read_file("input.txt")
    print(f"Résulat de la partie 1 : {part1(l)}")
    print(f"Résulat de la partie 2 : {part2(l)}")