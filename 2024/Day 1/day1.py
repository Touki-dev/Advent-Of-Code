INPUT = open("input.txt", "r")
INPUT = [(int(i.split('   ')[0]), int(i.split('   ')[1])) for i in INPUT.read().split('\n')]

def part1(l1, l2):
    total = 0
    for i in range(len(l1)):
        total += abs(min(l1)-min(l2))

        l1.pop(l1.index(min(l1)))
        l2.pop(l2.index(min(l2)))

    return total

def part2(l1, l2):
    print(len(l1))

    total = 0
    for i in range(len(l1)):
        augmentation = 0
        for j in range(len(l2)):
            if l1[i] == l2[j]:
                augmentation += 1

        total += l1[i] * augmentation
    return total

if __name__ == "__main__":
    l1 = list(map(lambda el: el[0], INPUT))
    l2 = list(map(lambda el: el[1], INPUT))
    print(f"Résulat de la partie 1 : {part1(list(l1), list(l2))}")
    print(f"Résulat de la partie 2 : {part2(l1, l2)}")

