import numpy as np

def read_file(file):
    with open(file, 'r') as file:
        return [list(line.strip()) for line in file]
       
def part1(l, word):
    rows = len(l)
    cols = len(l[0])
    word_len = len(word)
    total = 0
    
    # Directions: (dy, dx)
    directions = [
        (0, 1),    # droite
        (0, -1),   # gauche
        (1, 0),    # bas
        (-1, 0),   # haut
        (1, 1),    # diagonale bas-droite
        (1, -1),   # diagonale bas-gauche
        (-1, 1),   # diagonale haut-droite
        (-1, -1)   # diagonale haut-gauche
    ]
    
    def is_word_found(x, y, dx, dy):
        """Vérifie si le mot existe à partir de (x, y) dans la direction (dx, dy)."""
        for i in range(word_len):
            nx, ny = x + i * dx, y + i * dy
            if nx < 0 or ny < 0 or nx >= rows or ny >= cols:
                return False  # Hors de la grille
            if l[nx][ny] != word[i]:
                return False
        return True
    
    # Parcourir chaque case de la grille
    for x in range(rows):
        for y in range(cols):
            # Tester chaque direction
            for dx, dy in directions:
                if is_word_found(x, y, dx, dy):
                    total += 1
    
    return total

def part2(l):
    total = 0
    for i in range(1, len(l)-1):
        for j in range(1, len(l)-1):
            if l[i][j] == "A":
                if l[i-1][j-1] == "M" and l[i+1][j+1] == "S" or l[i-1][j-1] == 'S' and l[i+1][j+1] == 'M':
                    if l[i+1][j-1] == "M" and l[i-1][j+1] == 'S' or l[i+1][j-1] == 'S' and l[i-1][j+1] == 'M':
                        total += 1
    return total


    
if __name__ == "__main__":
    l = read_file("input.txt")
    print(f"Résulat de la partie 1 : {part1(l, "XMAS")}")
    print(f"Résulat de la partie 2 : {part2(l)}")
    