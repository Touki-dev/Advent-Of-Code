FORMAT = 2

def read_file(file):
    with open(file, 'r') as file:
        lignes = file.read().split('\n')
        if FORMAT == 0: # Lignes
            return lignes
        if FORMAT == 1: # Grid
            return list(map(list, lignes))
        if FORMAT == 2: # Custom
            return [(int(i.split(': ')[0]), list(map(int, i.split(': ')[1].split()))) for i in lignes]

from itertools import product

def calcul(eq, operateurs):
    total = eq[0]
    for i, op in enumerate(operateurs):
        if op == 0:
            total += eq[i+1]
        elif op == 1:
            total *= eq[i+1]
        elif op == 2:
            c = str(total) + str(eq[i+1])
            total = int(c)
    return total

def testLigne(ligne):
    result = ligne[0]
    eq = ligne[1]
    n_operateurs = len(eq) - 1
    
    for operateurs in product([0, 1], repeat=n_operateurs):
        if calcul(eq, operateurs) == result:
            return True
    
    return False

def testLigne2(ligne):
    result = ligne[0]
    eq = ligne[1]
    n_operateurs = len(eq) - 1
    
    for operateurs in product([0, 1, 2], repeat=n_operateurs):
        print(operateurs)
        if calcul(eq, operateurs) == result:
            return True
    
    return False

def part1(l):
    total = 0
    for i, ligne in enumerate(l):
        if testLigne(ligne):
            total += ligne[0]
    return total
            

def part2(l):
    total = 0
    for i, ligne in enumerate(l):
        if testLigne2(ligne):
            total += ligne[0]
    return total

if __name__ == "__main__":
    l = read_file("input.txt")
    print(f"Résulat de la partie 1 : {part1(l)}")
    print(f"Résulat de la partie 2 : {part2(l)}")