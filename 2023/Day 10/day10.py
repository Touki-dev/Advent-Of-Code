import numpy as np

data = open("data.txt", "r")
data = data.read().split('\n')

sketch = np.array([[data[i][j] for j in range(len(data[i]))] for i in range(len(data))])
bends = ["F", "7", 
         "L", "J"]

start = np.where(sketch == "S")
start = (start[0][0], start[1][0])

adjacents = [sketch[start[0]-1, start[1]], 
                 sketch[start[0], start[1]-1], sketch[start[0], start[1]+1], 
                 sketch[start[0]+1, start[1]]]

boxe = [start]
if adjacents[0] == "F" or adjacents[0] == "7" or adjacents[0] == "|":
    boxe = [(start[0]-1, start[1]), adjacents[0]]
if adjacents[1] == "F" or adjacents[1] == "L" or adjacents[1] == "-":
    boxe = [(start[0], start[1]-1), adjacents[1]]
if adjacents[2] == "J" or adjacents[2] == "7" or adjacents[2] == "-":
    boxe = [(start[0], start[1]+1), adjacents[2]]
if adjacents[3] == "L" or adjacents[3] == "J" or adjacents[3] == "|":
    boxe = [(start[0]+1, start[1]), adjacents[3]]

print(sketch[boxe[0][0], boxe[0][1]])

stop = False
while not stop:
    
    stop = True