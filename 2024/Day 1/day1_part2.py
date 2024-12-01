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
    augmentation = 0
    for j in range(len(l2)):
        if l1[i] == l2[j]:
            augmentation += 1
            
    total += l1[i] * augmentation
    
print(total)