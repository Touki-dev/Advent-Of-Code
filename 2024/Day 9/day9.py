#!/usr/bin/env pypy3

FORMAT = 2

def read_file(file):
    with open(file, 'r') as file:
        lignes = file.read().split('\n')
        if FORMAT == 0: # Lignes
            return lignes
        if FORMAT == 1: # Grid
            return list(map(list, lignes))
        if FORMAT == 2: # Custom
            return ''.join(lignes)


def part1(l):
    ...

def part2(l):
    ...

if __name__ == "__main__":
    l = read_file("input.txt")
    print(f"Résulat de la partie 1 : {part1(l) == 6356833654075}")
    print(f"Résulat de la partie 2 : {part2(l) == 6389911791746}")