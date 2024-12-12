from itertools import product

def read_file(file):
    with open(file, 'r') as file:
        lignes = file.read().split('\n')
        return [ligne.split() for ligne in lignes]

def testPos(ressorts, conditions, pos):
    if:
        ...

def part1(l):
    for ligne in l:
        ressorts = ligne[0]
        conditions = ligne[1]
        pos_inconnus = [i for i in range(len(ressorts)) if ressorts[i] == '?']
        
        for pos in product(pos_inconnus, repeat=len(pos_inconnus)):
            if pos != tuple(0 for _ in range(len(pos_inconnus))):
                
            
def part2(l):
    ...

if __name__ == "__main__":
    l = read_file("input.txt")
    print(f"Résulat de la partie 1 : {part1(l)}")
    print(f"Résulat de la partie 2 : {part2(l)}")