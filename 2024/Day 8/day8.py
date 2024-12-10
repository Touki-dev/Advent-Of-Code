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
    antennes = {}
    for i, ligne in enumerate(l):
        for j, el in enumerate(ligne):
            if el != ".":
                if antennes.get(el, None) is None:
                    antennes[el] = [(i, j)]
                else:
                    antennes[el].append((i, j))
    
    antinoeuds = set()
    for ant in antennes:
        for i in range(len(antennes[ant])):
            for j in range(i+1, len(antennes[ant])):
                # Vérifie alignement et calcule dist
                if antennes[ant][i][0] == antennes[ant][j][0]:  # Alignés horizontalement
                    dist = (0, antennes[ant][j][1] - antennes[ant][i][1])
                elif antennes[ant][i][1] == antennes[ant][j][1]:  # Alignés verticalement
                    dist = (antennes[ant][j][0] - antennes[ant][i][0], 0)
                else:  # Alignés diagonalement
                    dist = (antennes[ant][j][0] - antennes[ant][i][0], antennes[ant][j][1] - antennes[ant][i][1])

                # Calcule positions des antinœuds
                an1 = (antennes[ant][i][0] - dist[0], antennes[ant][i][1] - dist[1])
                an2 = (antennes[ant][j][0] + dist[0], antennes[ant][j][1] + dist[1])
                
                # Vérifie que les antinœuds sont valides
                for an in [an1, an2]:
                    if 0 <= an[0] < len(l) and 0 <= an[1] < len(l[0]):
                        antinoeuds.add(an)

    return len(antinoeuds)


def part2(l):
    antennes = {}
    for i, ligne in enumerate(l):
        for j, el in enumerate(ligne):
            if el != ".":
                if antennes.get(el, None) is None:
                    antennes[el] = [(i, j)]
                else:
                    antennes[el].append((i, j))
    
    antinoeuds = set()
    for ant in antennes:
        for i in range(len(antennes[ant])):
            for j in range(i+1, len(antennes[ant])):
                # Vérifie alignement et calcule dist
                if antennes[ant][i][0] == antennes[ant][j][0]:  # Alignés horizontalement
                    dist = (0, antennes[ant][j][1] - antennes[ant][i][1])
                elif antennes[ant][i][1] == antennes[ant][j][1]:  # Alignés verticalement
                    dist = (antennes[ant][j][0] - antennes[ant][i][0], 0)
                else:  # Alignés diagonalement
                    dist = (antennes[ant][j][0] - antennes[ant][i][0], antennes[ant][j][1] - antennes[ant][i][1])

                # Calcule positions des antinœuds
                an1 = [antennes[ant][i][0] - dist[0], antennes[ant][i][1] - dist[1]]
                an2 = [antennes[ant][j][0] + dist[0], antennes[ant][j][1] + dist[1]]
                
                # Vérifie que les antinœuds sont valides
                for n in range(2):
                    an = [an1, an2][n]
                    stop = False
                    while not stop:
                        if 0 <= an[0] < len(l) and 0 <= an[1] < len(l[0]):
                            antinoeuds.add(tuple(an))
                        else:
                            stop = True

                        if n == 0:
                            an[0] -= dist[0]
                            an[1] -= dist[1]
                        else:
                            an[0] += dist[0]
                            an[1] += dist[1]
    
    # Étape 3 : Ajoute toutes les antennes elles-mêmes si elles ne sont pas isolées
    for ant in antennes:
        if len(antennes[ant]) > 1:
            antinoeuds.update(antennes[ant])
    
    for an in antinoeuds:
        if 0<=an[0]<len(l) and 0<=an[1]<len(l[0]):
            l[an[0]][an[1]] = "#"
    
    print("\n".join(["".join(i) for i in l]))

    return len(antinoeuds)

if __name__ == "__main__":
    l = read_file("input.txt")
    print(f"Résulat de la partie 1 : {part1(l)}")
    print(f"Résulat de la partie 2 : {part2(l)}")