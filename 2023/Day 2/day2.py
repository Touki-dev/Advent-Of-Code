data = open("data.txt", "r")
data = data.read().split('\n')
condition = {
    'red': 12,
    'green': 13,
    'blue': 14
}
somme = 0

for i in range(len(data)):
    game = data[i].split(': ')
    n_game = game[0][5:]
    semicolons = game[1].split('; ')
    
    for j in range(len(semicolons)):
        colors = semicolons[j].split(', ')
        
        for k in range(len(colors)):
            n = colors[k].split(' ')[0]
            color = colors[k].split(' ')[1]
            
            if int(n) > condition[color]:
                n_game = str(0)
                
    somme += int(n_game)

print(somme)