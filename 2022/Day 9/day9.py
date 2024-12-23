def read_file(file):
    with open(file, 'r') as file:
        monkeys = file.read().split('\n\n')
        return [monkey.split('\n') for monkey in monkeys]

def part1(l):
    total_inspect = [0 for i in l]
    all_items = [list(map(int, monkey[1].split(': ')[1].split(', '))) for monkey in l]
    for i in range(20):
        for monkey in l:
            num = int(monkey[0].split(' ')[-1][-2])
            items = all_items[num]
            operation = monkey[2].split(' = ')[1]
            test = int(monkey[3].split(' ')[-1])
            
            for item in items:
                total_inspect[num] += 1
                new = eval(operation, {"old": item})
                new = new // 3
                
                if new % test == 0:
                    target = int(monkey[4].split(' ')[-1])
                else:
                    target = int(monkey[5].split(' ')[-1])
                    
                all_items[target].append(new)
            
            all_items[num] = []
            
    biggers = sorted(range(len(total_inspect)), key=lambda i: total_inspect[i], reverse=True)[:2]
    return total_inspect[biggers[0]] * total_inspect[biggers[1]]
    
def part2(l):
    total_inspect = [0 for i in l]
    all_items = [list(map(int, monkey[1].split(': ')[1].split(', '))) for monkey in l]
    for i in range(1):
        for monkey in l:
            num = int(monkey[0].split(' ')[-1][-2])
            items = all_items[num]
            operation = monkey[2].split(' = ')[1]
            test = int(monkey[3].split(' ')[-1])
            
            for item in items:
                total_inspect[num] += 1
                new = eval(operation, {"old": item})
                
                if new % test == 0:
                    target = int(monkey[4].split(' ')[-1])
                else:
                    target = int(monkey[5].split(' ')[-1])
                    
                all_items[target].append(new)
            
            all_items[num] = []
            
    biggers = sorted(range(len(total_inspect)), key=lambda i: total_inspect[i], reverse=True)[:2]
    return total_inspect[biggers[0]], total_inspect[biggers[1]]

if __name__ == "__main__":
    l = read_file("input.txt")
    print(f"Résulat de la partie 1 : {part1(l)}")
    print(f"Résulat de la partie 2 : {part2(l)}")