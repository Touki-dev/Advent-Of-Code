data = open("data.txt", "r")
data = data.read().split('\n')

cal_lutins = [0]
i = 0

for cal in data:
    if cal == "":
        cal_lutins.append(0)
        i+=1
    else:
        cal_lutins[i] += int(cal)

total = 0
for i in range(3):
    total += max(cal_lutins)
    cal_lutins.pop(cal_lutins.index(max(cal_lutins)))
    
print(total)