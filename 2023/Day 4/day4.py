data = open("data.txt", "r")
data = data.read().split('\n')

somme = 0
for i in range(len(data)):
    n_card = i+1
    numeros = data[i].split(": ")[1]
    numeros_gagnants = list(map(int, filter(None, numeros.split("|")[0].split(" "))))
    numeros_grattés = list(map(int, filter(None, numeros.split("|")[1].split(" "))))
    
    n=0
    for j in numeros_grattés:
        if j in numeros_gagnants:
            if n==0:
                n=1
            else:
                n=n*2
    somme += n
    
print(somme)