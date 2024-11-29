data = open("data.txt", "r")
data = data.read().split('\n')
i=0

cards = [{"num": i+1, "nb": 0} for i in range(len(data))]
cards[0]["nb"] = 1

total = 0
for i in range(len(data)):
    n_card = i+1
    nb_cards = cards[i]['nb']
            
    numeros = data[i].split(": ")[1]
    numeros_gagnants = list(map(int, filter(None, numeros.split("|")[0].split(" "))))
    numeros_grattés = list(map(int, filter(None, numeros.split("|")[1].split(" "))))
        
    count = 0
    for k in numeros_grattés:
        if k in numeros_gagnants:
            count += 1
            if i + count < len(cards):
                cards[i + count]['nb'] += nb_cards
                total += int(nb_cards)
            
print(total, cards)