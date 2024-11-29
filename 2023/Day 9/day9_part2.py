data = open("data.txt", "r")
data = data.read().split('\n')

somme = 0

for i in range(len(data)):
    sequences = [list(map(int, data[i].split(" ")))]
    j=0
    while sum(sequences[-1]) != 0:
        new_sequence = [sequences[j][k] - sequences[j][k-1] for k in range(1, len(sequences[j]))]
        sequences.append(new_sequence)
        j+=1
        
    for k in range(len(sequences)-1,0,-1):
        sequences[k-1].insert(0,sequences[k-1][0]-sequences[k][0])
    
    somme += sequences[0][0]

print(somme)