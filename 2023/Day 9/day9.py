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
    
    prediction = 0
    for j in range(len(sequences)-1,-1,-1):
        prediction += sequences[j][-1]
        
    somme += prediction

print(somme)