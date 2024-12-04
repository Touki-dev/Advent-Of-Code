def read_file(file):
    with open(file, 'r') as file:
        return file.read().split('\n')

l = read_file("input.txt")
total = 0
table = {
    "2": 2,
    "1": 1,
    "0": 0,
    "-": -1,
    "=": -2,
}

for ligne in l:
    n = 0
    for i in range(len(ligne)):
        caract = ligne[len(ligne)-1-i]
        n += table[caract] * (5**i)
    total += n

print(total)
table = {
    2: "2",
    1: "1",
    0: "0",
    -1: "-",
    -2: "=",
}

base=5
result = []
while total != 0:
    remainder = total % base
    
    # Adapter les restes pour qu'ils tombent dans la plage [-2, 2]
    if remainder > 2:
        remainder -= base
    result.append(table[remainder])
    
    # Mettre à jour le nombre en tenant compte du reste ajusté
    total = (total - remainder) // base
        
print("".join(reversed(result)))
