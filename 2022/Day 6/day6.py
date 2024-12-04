def read_file(file):
    with open(file, 'r') as file:
        return file.read()
    
def part1(l):
    memoire = []
    for i, c in enumerate(l):
        memoire.append(c)
        if len(memoire) > 4:
            memoire.pop(0)
            
        if len(set(memoire)) == len(memoire) and len(memoire) == 4:
            print(i+1)
            break

def part2(l):
    memoire = []
    for i, c in enumerate(l):
        memoire.append(c)
        if len(memoire) > 14:
            memoire.pop(0)
            
        if len(set(memoire)) == len(memoire) and len(memoire) == 14:
            print(i+1)
            break

l = read_file("input.txt")
part1(l)
part2(l)