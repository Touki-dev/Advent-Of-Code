data = open("data.txt", "r")
data = data.read().split('\n')

instructions = data[0]
dict_nodes = {
    data[i].split(' = ')[0]: tuple(data[i].split(' = ')[1].strip("()").split(", "))
    for i in range(2, len(data))
}

node = "AAA"

i = 0
while node != "ZZZ":
    instr = instructions[i%len(instructions)]
    destination = dict_nodes[node]
    if instr == 'L':
        node = destination[0]
    else:
        node = destination[1]
    i += 1
    print(node)

print(i)