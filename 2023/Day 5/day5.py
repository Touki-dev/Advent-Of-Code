data = open("data.txt", "r")
data = data.read()

seeds = list(map(int, data.split("\n")[0].split(": ")[1].split(" ")))
convert_seeds = []

for i in range(len(seeds)):
    seed = int(seeds[i])
    destination = seed
    categories = data.split(':\n')
    
    for j in range(1, len(categories)):
        categorie = categories[j]
        plages = list(filter(None, categorie.split('\n')))
        plages.pop(-1)
        
        for k in range(len(plages)):
            categorie = list(map(int, plages[k].split(' ')))
            if categorie[1] <= seed and seed <= categorie[1] + categorie[2]-1:
                seed = categorie[0] + (seed - categorie[1])
                
    convert_seeds.append(seed)

print(min(convert_seeds))