data = open("data.txt", "r")
data = data.read().split('\n')

l1 = []
l2 = []
for i in range(len(data)):
    nombres = data[i].split('   ')
    n1 = nombres[0]
    n2 = nombres[1]
    
    l1.append(int(n1))
    l2.append(int(n2))

total = 0
for i in range(len(l1)):
    total += abs(min(l1)-min(l2))
    
    l1.pop(l1.index(min(l1)))
    l2.pop(l2.index(min(l2)))
    
print(total)