data = open("data.txt", "r")
data = data.read().split('\n')
all_numbers = []

arr_number = ['one','two','three','four','five','six','seven','eight','nine']

for i in range(len(data)):
    number = []
    print(data[i])
    for j in range(len(arr_number)):
        data[i] = data[i].split(arr_number[j])
        for k in range(len(data[i])):
            for l in range(len(arr_number)):
                if len((data[i][k] + arr_number[j][0]).split(arr_number[l])) > 1:
                    data[i][k] = str(l).join((data[i][k] + arr_number[j][0]).split(arr_number[l]))
        data[i] = str(j+1).join(data[i])
    print(data[i])
    for j in range(len(data[i])):
        if data[i][j].isdigit():
            number.append(data[i][j])
    print(number[0] + number[-1])
    all_numbers.append(number[0] + number[-1])

somme = 0
for i in range(len(all_numbers)):
    somme += int(all_numbers[i])

print(somme)