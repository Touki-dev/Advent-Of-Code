import numpy as np

def read_file(file):
    with open(file, 'r') as file:
        return [list(line.strip()) for line in file]
       
def part1(l):
    ...

def part2(l):
    ...
    
if __name__ == "__main__":
    l = read_file("input.txt")
    print(f"Résulat de la partie 1 : {part1(l)}")
    print(f"Résulat de la partie 2 : {part2(l)}")