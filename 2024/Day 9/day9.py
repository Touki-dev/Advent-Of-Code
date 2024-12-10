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
    arr = []
    file_id = 0
    empties = []

    for i, size in enumerate(map(int, l)):
        if i % 2 == 0:
            arr.extend([file_id] * size)
            file_id += 1
        else:
            empties.extend(list(range(len(arr), len(arr) + size)))
            arr.extend(["."] * size)
            
    empty_idx = 0
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == ".":
            continue

        to = empties[empty_idx]
        empty_idx += 1
        if to >= i:
            break
        
        arr[to] = arr[i]
        arr[i] = ""

    total = 0
    for i, n in enumerate(arr):
        if n != ".":
            total += i * n
    
    return total

def part2(l):
    ...

if __name__ == "__main__":
    l = read_file("input.txt")
    print(f"Résulat de la partie 1 : {part1(l) == 6356833654075}")
    print(f"Résulat de la partie 2 : {part2(l) == 6389911791746}")