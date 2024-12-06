from tqdm import tqdm
import numpy as np
from concurrent.futures import ThreadPoolExecutor

data = open("input.txt", "r")
data = data.read().split('\n')

def hexToBase10(n):
    codeHex = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15
    }
    n_base10 = 0
    for i, bit in enumerate(n): n_base10 += codeHex[bit] * (16 ** (len(n) - i - 1))
    return n_base10

def digger(data):
    polygon = []
    pos = (0, 0)
    sommets = []
    max_x, max_y, min_x, min_y = 0, 0, 0, 0

    for i in tqdm(range(len(data)), desc="Parsing data"): 
        data[i] = data[i].split(' ')  
        codeHex = data[i][2]
        direction = codeHex[7]
        n = codeHex[2:7]
        n = hexToBase10(n)
        
        for j in range(n):
            if direction == '3':
                pos = (pos[0], pos[1] - 1)
            elif direction == '1':
                pos = (pos[0], pos[1] + 1)
            elif direction == '2':
                pos = (pos[0] - 1, pos[1])
            else:
                pos = (pos[0] + 1, pos[1])
                
            if j == n - 1:
                sommets.append(pos)
        
        if pos[0] > max_x:
            max_x = pos[0]
        if pos[1] > max_y:
            max_y = pos[1]
        if pos[0] < min_x:
            min_x = pos[0]
        if pos[1] < min_y:
            min_y = pos[1]
        
        polygon.append(pos)
        
    return polygon, sommets, max_x, max_y, min_x, min_y

def listToNumpy(polygon):
    grouped_coords = {}
    for x,y in polygon:
        if x not in grouped_coords:
            grouped_coords[x] = []
        grouped_coords[x].append(y)
    
    grouped_coords = {k: np.array(v) for k, v in grouped_coords.items()}
    return grouped_coords

# Calcul de l'aire avec multithreading
def calculate_area(polygon, max_x, max_y, min_x, min_y):
    def process_row(x):
        inside = 0
        row_area = 0
        print("row", x - min_x, "/", max_x-min_x, "...")
        for y in range(min_x, max_x + 1):
            if x in polygon.keys():
                if y in polygon[x]:
                    inside += 1
                    row_area += 1
                elif inside % 2 == 1:
                    row_area += 1
        
        return row_area

    # Utilisation d'un pool de threads pour paralléliser les lignes
    with ThreadPoolExecutor() as executor:
        row_areas = list(tqdm(
            executor.map(process_row, range(min_x, max_x + 1)),
            total=(max_y - min_y + 1),
            desc="Calculating area"
        ))
    
    # Calcul final de l'aire
    return sum(row_areas)

# Appel des fonctions
polygon, sommets, max_x, max_y, min_x, min_y = digger(data)
polygon = listToNumpy(polygon)
area = calculate_area(polygon, max_x, max_y, min_x, min_y)
print(area)