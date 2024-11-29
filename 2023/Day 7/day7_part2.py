data = open("data.txt", "r")
data = data.read().split('\n')

power = ("A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J")
power_without_J = ("A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2")
power_index = {card: i for i, card in enumerate(power)}

types = ([5], [4,1], [3,2], [3,1,1], [2,2,1], [2,1,1,1], [1,1,1,1,1])

power_hands = [[],[],[],[],[],[],[]]

for i in range(len(data)):
    hand = data[i].split(' ')[0]
    
    N_joker = 0
    N_cards = {j: 0 for j in power_without_J}
    
    for card in hand:
        if card == "J":
            N_joker += 1
        else:
            N_cards[card] += 1
    
    type_hand = []
    for key in N_cards:
        if N_cards[key] > 0:
            type_hand.append(N_cards[key])
    
    if len(type_hand) == 0:
        type_hand = [5]
    else:
        type_hand[type_hand.index(max(type_hand))] += N_joker
    
    print(hand, N_joker, type_hand)
    
    for type in types:
        if sorted(type_hand, reverse=True) == type:
            type_hand = types.index(type)
            break
            
    power_hands[type_hand].append({
        "hand": hand,
        "bid_amount": data[i].split(' ')[1]
    })

for i in range(len(power_hands)):
    power_hands[i] = sorted(power_hands[i], key=lambda hand: [power_index[card] for card in hand["hand"]])
    
power_hands = [item for sublist in power_hands for item in sublist]
total = 0
for i in range(len(power_hands)):
    total += int(power_hands[i]["bid_amount"]) * (len(power_hands)-i)
print(total)