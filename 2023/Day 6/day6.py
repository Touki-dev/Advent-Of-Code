data = open("data.txt", "r")
data = data.read().split('\n')
N_races = len(list(filter(None, data[0].split(' '))))
product = 1

for i in range(1, N_races):
    time = int(list(filter(None, data[0].split(' ')))[i])
    record = int(list(filter(None, data[1].split(' ')))[i])
    options = []
    
    for j in range(time):
        distance_parcouru = (time - j) * j
        if distance_parcouru > record:
            options.append(j)
    
    product = product * len(options)
print(product)