data = open("data.txt", "r")
data = data.read().split('\n')

coord_galaxies = []
galaxies_check = []
all_distances = []

for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == "#":
            coord_galaxies.append((i,j))

print(len(coord_galaxies))
            
for i, coord in enumerate(coord_galaxies):
    index = len(coord_galaxies)-(i+1)
    galaxies_check.append(coord)
    for j in range(index):
        if coord_galaxies[j] not in galaxies_check:
            distance = abs(coord_galaxies[j][0] - coord[0]) + abs(coord_galaxies[j][1] - coord[1])
            all_distances.append(distance)