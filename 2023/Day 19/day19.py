def read_file(file):
    with open(file, 'r') as file:
        lignes = file.read().split('\n\n')
        return [i for i in lignes]

def tri(workflows, dict_note):
    ...
    
def part1(l):
    notes = [i.strip("{}").split(",") for i in l[1].split("\n")]
    
    all_notes = []
    for note in notes:
        dict_note = {}
        for el in note:
            print(el)
            key, value = el.split("=")
            dict_note[key.strip()] = int(value.strip())
        all_notes.append(dict_note)
    
    for i in all_notes:
        accept = tri()

def part2(l):
    ...

if __name__ == "__main__":
    l = read_file("input.txt")
    print(f"Résulat de la partie 1 : {part1(l)}")
    print(f"Résulat de la partie 2 : {part2(l)}")