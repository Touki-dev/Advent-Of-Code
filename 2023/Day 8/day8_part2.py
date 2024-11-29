data = open("data.txt", "r")
data = data.read().split('\n')

instructions = data[0]
dict_nodes = {
    data[i].split(' = ')[0]: tuple(data[i].split(' = ')[1].strip("()").split(", "))
    for i in range(2, len(data))
}

nodes = []
for i in range(ord("A"), ord("Z")+1):
    for j in range(ord("A"), ord("Z")+1):
        node = chr(i)+chr(j)+"A"
        if node in dict_nodes.keys():
            nodes.append(node)
            
print(nodes)

i = 0
while not all(node.endswith("Z") for node in nodes):
    instr = instructions[i%len(instructions)]
    for node in nodes:
        destination = dict_nodes[node]
        if instr == 'L':
            node = destination[0]
        else:
            node = destination[1]
        if node.endswith("Z"):
            print(i)
    i += 1

print(i)