data = open("data.txt", "r")
data = data.read().split('\n')

def digger(data):
    trous = [(0,0)]
    pos = (0,0)
    sommets = []

    for i in range(len(data)):
        data[i] = data[i].split(' ')
        
        direction = data[i][0]
        n = int(data[i][1])
        color = data[i][2]
        
        for j in range(n):
            if direction == 'U':
                pos = (pos[0], pos[1]-1)
            elif direction == 'D':
                pos = (pos[0], pos[1]+1)
            elif direction == 'L':
                pos = (pos[0]-1, pos[1])
            else:
                pos = (pos[0]+1, pos[1])
                
            if j == n-1:
                sommets.append(pos)
            trous.append(pos)
    
    return trous, sommets

def make_map(coordinates, sommets):
    # Dimensions de la carte (modifiable selon les besoins)
    map_width = max(x for x, _ in coordinates) + abs(min(x for x, _ in coordinates))
    map_height = max(y for _, y in coordinates) + abs(min(y for _, y in coordinates))

    # Création d'une grille vide (remplie d'espaces ou de points pour la visualisation)
    grid = [["." for _ in range(map_width+1)] for _ in range(map_height+1)]

    # Remplissage de la grille avec les coordonnées
    for x, y in coordinates:
        if (x,y) in sommets:
            grid[y + abs(min(y for _, y in coordinates))][x + abs(min(x for x, _ in coordinates))] = "@"
        else:
            grid[y + abs(min(y for _, y in coordinates))][x + abs(min(x for x, _ in coordinates))] = "#"

    # Affichage de la carte
    with open("map.txt", "w") as file:
        for row in grid:
            file.write("".join(row) + "\n")
    
    return grid

def is_point_inside_polygon(x, y, polygon):
    n = len(polygon)
    inside = False
    px, py = x, y
    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % n]
        if ((y1 > py) != (y2 > py)) and (px < (x2 - x1) * (py - y1) / (y2 - y1) + x1):
            inside = not inside
    return inside

def calculate_area(trous):
    # Détection des limites de la grille
    min_x = min(x for x, _ in trous)
    max_x = max(x for x, _ in trous)
    min_y = min(y for _, y in trous)
    max_y = max(y for _, y in trous)
    
    area = 0
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            if ((x, y) in trous) or is_point_inside_polygon(x, y, trous):
                area += 1
    return area

trous, sommets = digger(data)
make_map(trous, sommets)
area = calculate_area(trous)
print(area)