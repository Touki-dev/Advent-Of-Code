def read_file(file):
    with open(file, 'r') as file:
        lignes = file.read().split('\n\n')
        return [ligne.split('\n') for ligne in lignes]

def part1(l):
    inputs = [i.split(": ") for i in l[0]]
    gates = [i.split(" ") for i in l[1]]
    
    inputs_dico = {i[0]:int(i[1]) for i in inputs}
    for gate in gates:
        if gate[0] in inputs_dico and gate[2] in inputs_dico:
            op = gate[1]
            if (op == "AND" and (inputs_dico[gate[0]] and inputs_dico[gate[2]])) or (op == "OR" and (inputs_dico[gate[0]] or inputs_dico[gate[2]])) or (op == "XOR" and (inputs_dico[gate[0]] != inputs_dico[gate[2]])):
                inputs_dico[gate[4]] = 1
            else:
                inputs_dico[gate[4]] = 0
        else:
            gates.append(gate)
    
    bits = []
    for input in sorted(inputs_dico.keys()):
        if input[0] == "z":
            bits.insert(0, str(inputs_dico[input]))
            
    return int("".join(bits), 2)

def part2(l):
    ...

if __name__ == "__main__":
    l = read_file("input.txt")
    print(f"Résulat de la partie 1 : {part1(l)}")
    print(f"Résulat de la partie 2 : {part2(l)}")