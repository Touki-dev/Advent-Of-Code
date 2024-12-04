import sympy

def read_file(file):
    with open(file, 'r') as file:
        return [(tuple(map(int, i[0].split(', '))), tuple(map(int, i[1].split(', ')))) for i in (line.split(' @ ') for line in file)]

def part1(l, zoneTest):
    hailstones = []
    for hs in l:
        # paramètre de l'equation y = mx+p
        m = hs[1][1] / hs[1][0]
        p = hs[0][1] - m * hs[0][0]
        hailstones.append({ "m": m, "p": p, "px": hs[0][0], "py": hs[0][1], "vx": hs[1][0], "vy": hs[1][1] })
      
    total = 0
    for i, hs1 in enumerate(hailstones):
        for hs2 in hailstones[:i]:
            m1, p1, m2, p2 = hs1["m"], hs1["p"], hs2["m"], hs2["p"]
            if m1 != m2:
                x = (p2 - p1)/(m1 - m2)
                y = m1*x + p1
                
                if (zoneTest[0] <= x <= zoneTest[1]) and (zoneTest[0] <= y <= zoneTest[1]):
                    if all((x - hs["px"]) * hs["vx"] >= 0 and (y - hs["py"]) * hs["vy"] >= 0 for hs in (hs1, hs2)):
                        total += 1
    
    return total

def part2(l):
    # Solution de @hyper-neutrino, commenté par chat-GPT
    # Chargement des grêlons depuis l'entrée standard (ou fichier), chaque ligne contient la position et la vitesse initiale.
    hailstones = [tuple(map(int, line.replace("@", ",").split(","))) for line in open("input.txt")]
    # Déclaration des variables symboliques pour la position et la vitesse du rocher
    xr, yr, zr, vxr, vyr, vzr = sympy.symbols("xr, yr, zr, vxr, vyr, vzr")
    # Liste pour accumuler les équations linéaires
    equations = []

    # Parcours de tous les grêlons pour construire les équations de collision
    for i, (sx, sy, sz, vx, vy, vz) in enumerate(hailstones):
        # Première équation : relation entre les positions initiales et les vitesses sur les axes X et Y
        equations.append((xr - sx) * (vy - vyr) - (yr - sy) * (vx - vxr))
        # Deuxième équation : relation entre les positions initiales et les vitesses sur les axes Y et Z
        equations.append((yr - sy) * (vz - vzr) - (zr - sz) * (vy - vyr))
        
        # Ignorer les deux premiers grêlons (pas assez d'équations pour résoudre le système à ce stade)
        if i < 2:
            continue

        # Tentative de résolution du système d'équations
        answers = [
            soln for soln in sympy.solve(equations) # sympy.solve retourne une liste de solutions pour les variables symboliques
            if all(x % 1 == 0 for x in soln.values())  # On garde uniquement les solutions avec des valeurs entières
        ]
        
        # Si une solution unique est trouvée, arrêter le traitement (le problème est résolu)
        if len(answers) == 1:
            print(i)
            break

    # La première (et unique) solution trouvée
    answer = answers[0]
    # Calcul du résultat demandé : somme des coordonnées X, Y, Z de la position initiale du rocher
    return answer[xr] + answer[yr] + answer[zr], i


if __name__ == "__main__":
    l = read_file("input.txt")
    zoneTest = (200000000000000, 400000000000000)
    print(f"Résulat de la partie 1 : {part1(l, zoneTest)}")
    print(f"Résulat de la partie 2 : {part2(l)}")