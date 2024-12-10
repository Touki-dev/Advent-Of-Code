FORMAT = 1

def read_file(file):
    with open(file, 'r') as file:
        lignes = file.read().split('\n')
        if FORMAT == 0: # Lignes
            return lignes
        if FORMAT == 1: # Grid
            return list(map(list, lignes))
        if FORMAT == 2: # Custom
            return [(int(i.split(': ')[0]), list(map(int, i.split(': ')[1].split()))) for i in lignes]

def part1(l):
    ...


def part2(l):
    ...

if __name__ == "__main__":
    l = read_file("input.txt")
    print(f"Résulat de la partie 1 : {part1(l)}")
    print(f"Résulat de la partie 2 : {part2(l)}")