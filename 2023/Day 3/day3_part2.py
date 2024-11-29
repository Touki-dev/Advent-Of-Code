import numpy as np

data = open("data.txt", "r")
data = data.read().split('\n')
data = [" ".join(i).split(" ") for i in data]

not_symbols = ["0","1","2","3","4","5","6","7","8","9","."]
somme = 0
n = ""
arr = np.array([[1,2,3,4],[1,2,3,4]])
print(arr[0:][1:2])

for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == "*":
            interval = data[i-1:i+2][j-3:j+3]