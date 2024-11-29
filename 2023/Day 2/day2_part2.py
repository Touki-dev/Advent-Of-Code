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
    
    freq_color = {
        'red': [0],
        'green': [0],
        'blue': [0],
    }
    
    for j in range(len(semicolons)):
        colors = semicolons[j].split(', ')
        
        for k in range(len(colors)):
            n = colors[k].split(' ')[0]
            color = colors[k].split(' ')[1]
            
            freq_color[color].append(int(n))
    
    puissance = max(freq_color['red']) * max(freq_color['green']) * max(freq_color['blue'])
    somme += puissance

print(somme)