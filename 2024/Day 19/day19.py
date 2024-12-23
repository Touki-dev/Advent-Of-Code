from functools import lru_cache

def read_file(file):
    with open(file, 'r') as file:
        return file.read().split('\n\n')

l = read_file("input.txt")
modeles, motifs = l
modeles = modeles.split(", ")
motifs = motifs.split("\n")

@lru_cache(maxsize=None)
def checkMotif(motif):
    if motif == "":
        return 1
    res = 0
    for modele in modeles:
        if motif.startswith(modele):
            res += checkMotif(motif[len(modele):])
    return res

def part1():
    return sum([checkMotif(motif)>0 for motif in motifs])

def part2():
    return sum([checkMotif(motif) for motif in motifs])

if __name__ == "__main__":
    print(f"Résulat de la partie 1 : {part1()}")
    print(f"Résulat de la partie 2 : {part2()}")