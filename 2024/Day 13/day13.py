FORMAT = 1

def read_file(file):
    with open(file, 'r') as file:
        file = file.read().split('\n\n')
        return [machine.split("\n") for machine in file]

def count_X(coord_prize, coord_buttonA, coord_buttonB):
    for i in range(100):
        n_buttonA = 0
        n_buttonB = 0
        coord_prize_test = [int(coord_prize[0][2:]), int(coord_prize[1][2:])]
            
        for j in range(i):
            if coord_buttonA[0] < coord_buttonB[0]:
                coord_prize_test[0] -= coord_buttonA[0]
                coord_prize_test[1] -= coord_buttonA[1]
                n_buttonA += 1
            else:
                coord_prize_test[0] -= coord_buttonB[0]
                coord_prize_test[1] -= coord_buttonB[1]
                n_buttonB += 1
            
        while coord_prize_test[0] > 0:
            if coord_buttonA[0] > coord_buttonB[0]:
                coord_prize_test[0] -= coord_buttonA[0]
                coord_prize_test[1] -= coord_buttonA[1]
                n_buttonA += 1
            else:
                coord_prize_test[0] -= coord_buttonB[0]
                coord_prize_test[1] -= coord_buttonB[1]
                n_buttonB += 1
            
            if coord_prize_test[0] == 0 and coord_prize_test[1] == 0:
                return n_buttonA, n_buttonB
      
def count_Y(coord_prize, coord_buttonA, coord_buttonB):
    for i in range(100):
        n_buttonA = 0
        n_buttonB = 0
        coord_prize_test = [int(coord_prize[0][2:]), int(coord_prize[1][2:])]
            
        for j in range(i):
            if coord_buttonA[1] < coord_buttonB[1]:
                coord_prize_test[0] -= coord_buttonA[0]
                coord_prize_test[1] -= coord_buttonA[1]
                n_buttonA += 1
            else:
                coord_prize_test[0] -= coord_buttonB[0]
                coord_prize_test[1] -= coord_buttonB[1]
                n_buttonB += 1
            
        while coord_prize_test[1] > 0:
            if coord_buttonA[1] > coord_buttonB[1]:
                coord_prize_test[0] -= coord_buttonA[0]
                coord_prize_test[1] -= coord_buttonA[1]
                n_buttonA += 1
            else:
                coord_prize_test[0] -= coord_buttonB[0]
                coord_prize_test[1] -= coord_buttonB[1]
                n_buttonB += 1
            
            if coord_prize_test[0] == 0 and coord_prize_test[1] == 0:
                return n_buttonA, n_buttonB
                  
def count_button(coord_prize, coord_buttonA, coord_buttonB):
    coord_buttonA = list(map(lambda x: int(x[2:]), coord_buttonA))
    coord_buttonB = list(map(lambda x: int(x[2:]), coord_buttonB))
    
    res = count_X(coord_prize, coord_buttonA, coord_buttonB)
    if not res:
        return False
    nAX, nBX = res
    print(res)
    if not res:
        return False
    res = count_Y(coord_prize, coord_buttonA, coord_buttonB)
    nAY, nBY = res
    print(res, "\n")
    
    n_tokenX = nAX*3 + nBX*1
    n_tokenY = nAY*3 + nBY*1
    
    return min([n_tokenX, n_tokenY])

def part1(l):
    total = 0
    for machine in l:
        coord_buttonA = [i for i in machine[0].split(": ")[1].split(", ")]
        coord_buttonB = [i for i in machine[1].split(": ")[1].split(", ")]
        coord_prize = [i for i in machine[2].split(": ")[1].split(", ")]
        
        res = count_button(coord_prize, coord_buttonA, coord_buttonB)
        if res:
            total += res
            
    return total

def part2(l):
    ...

if __name__ == "__main__":
    l = read_file("input.txt")
    print(f"Résulat de la partie 1 : {part1(l)}")
    print(f"Résulat de la partie 2 : {part2(l)}")