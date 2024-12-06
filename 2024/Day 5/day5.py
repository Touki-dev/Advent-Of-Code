import numpy as np

def read_file(file):
    with open(file, 'r') as file:
        return file.read().split('\n\n')

def checkOrder(regles, memory, n):
    for k in regles[n]:
        if k in memory:
            return False
    return True
def part1(l, regles):
    total = 0
    cleanl = list(l)
    for ligne in l:
        ligne = ligne.split(',')
        memory = []
        for j, n in enumerate(ligne):
            if n in regles:
                if checkOrder(regles, memory, n) == False:
                    break
            memory.append(n)
        
        if len(memory) == len(ligne):
            total += int(ligne[len(ligne)//2])
            cleanl.pop(cleanl.index(",".join(ligne)))
    
    return total, cleanl

def part2(l, regles):
    _, l = part1(l, regles)
    total = 0
    for ligne in l:
        ligne = ligne.split(',')
        result = []
        attente = list(ligne)
        i=0
        while len(result) != len(ligne):
            n = attente[i % len(attente)]
            find = False
            for j in attente:
                if j in regles:
                    if n in regles[j]:
                        find = True
                        break
            if not find:
                result.append(n)
                if n in attente:
                    attente.pop(attente.index(n))
            i+=1
        print(result)
        total += int(result[len(result)//2])
    return total       
    
    
if __name__ == "__main__":
    l = read_file("input.txt")
    l[0] = l[0].split('\n')
    l[1] = l[1].split('\n')
    regles = {}
    for el in l[0]:
        el = el.split('|')
        if el[0] in regles:
            regles[el[0]].append(el[1])
        else:
            regles[el[0]] = [el[1]]
    
    print(f"Résulat de la partie 1 : {part1(l[1], regles)[0]}")
    print(f"Résulat de la partie 2 : {part2(l[1], regles)}")