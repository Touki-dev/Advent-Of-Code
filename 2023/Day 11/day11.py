import numpy as np

l = open("data.txt", "r")
l = l.read().split('\n')

l_develop = np.array([list(i) for i in l])
coord_galaxies = []
all_distances = []

for i, ligne in enumerate(l):
    ligne = list(ligne)
    if "#" not in ligne:
        l_develop = np.insert(l_develop, i, ["".join(ligne)], axis=0)

for i in range(len(l_develop[0])):
    if np.all(l_develop[i, :] == "."):
        print(i)
        l_develop = np.insert(l_develop, i, np.full((len(l_develop), 1), "."), axis=1)


for coord in np.ndindex(l_develop.shape):
    if l_develop[coord] == "#":
        coord_galaxies.append(coord)
        
for i, gal1 in enumerate(coord_galaxies):
    coord_galaxies[i] = None
    
    for j, gal2 in enumerate(coord_galaxies):
        if gal2 != None:
            distX = abs(gal2[0] - gal1[0])+1
            distY = abs(gal2[1] - gal1[1])+1
            all_distances.append(distX + distY)

print(sum(all_distances))