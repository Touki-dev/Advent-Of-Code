import numpy as np

def read_file(file):
    with open(file, 'r') as file:
        file = file.read().split('\n\n')
        return [machine.split("\n") for machine in file]

def part1(l):
    total = 0
    for machine in l:
        coord_buttonA = [i for i in machine[0].split(": ")[1].split(", ")]
        coord_buttonB = [i for i in machine[1].split(": ")[1].split(", ")]
        coord_prize = [i for i in machine[2].split(": ")[1].split(", ")]

        a = np.array([list(map(int, [coord_buttonA[0][2:], coord_buttonB[0][2:]])), list(map(int, [coord_buttonA[1][2:], coord_buttonB[1][2:]]))])
        b = np.array(list(map(lambda x: int(x[2:]),coord_prize)))
        x = np.linalg.solve(a, b)

        if x[0] % 1 == 0 and x[1] % 1 == 0:
            print(x[0]*3 + x[1])
            total += x[0]*3 + x[1]

    return total

def part2(l):
    ...

if __name__ == "__main__":
    l = read_file("input.txt")
    print(f"Résulat de la partie 1 : {part1(l)}")
    print(f"Résulat de la partie 2 : {part2(l)}")
