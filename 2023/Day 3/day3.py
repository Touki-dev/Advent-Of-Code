data = open("data.txt", "r")
data = data.read().split('\n')

not_symbols = ["0","1","2","3","4","5","6","7","8","9","."]
somme = 0
n = ""

for i in range(len(data)):
    data[i] += "."

for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j].isdigit():
            n += (data[i][j])
        else:
            if n != "":
                symbol = False
                adjacents = []
                for k in range(i-1,i+2):
                    for l in range(j-len(n)-1, j+1):
                        if k >= 0 and k < len(data) and l >=0 and l < len(data[i]):
                            if data[k][l] not in not_symbols:
                                symbol = True
                                break
                    if symbol:
                        break
                if symbol:
                    somme += int(n)
                n = ""

print(somme)