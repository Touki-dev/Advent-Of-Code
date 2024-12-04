MODE = 0

def read_file(file):
    with open(file, 'r') as file:
        if MODE == 0:
            # return list of strings
            return [line.strip() for line in file]
        elif MODE == 1:
            # return list of tuples of strings
            return [tuple(line.strip().split()) for line in file]
        elif MODE == 2:
            # return list of integers
            return [int(line) for line in file]
        elif MODE == 3:
            # return list of digits in 2D list
            return [list(map(int, list(line.strip()))) for line in file]
        elif MODE == 4:
            # return list of tuples of integers
            return [tuple(map(int, line.strip().split())) for line in file]

import re

def part1(l):
    result = 0
    for i in range(len(l)):
        matches = re.findall(r"mul\((\d+),(\d+)\)", l[i])
        
        for match in matches:
            num1, num2 = map(int, match)
            result = result + (num1 * num2)
    return result
            
def part2(l):
    result = 0
    enabled = True
    for i in range(len(l)):
        matches = re.findall(r"(do\(\)|don't\(\)|mul\(\d+,\d+\))", l[i])

        for match in matches:
            match = match.strip()
            if match == 'do()':
                enabled = True
            elif match == "don't()":
                enabled = False
            elif match.startswith("mul") and enabled:
                match = re.match(r"mul\((\d+),(\d+)\)", match)
                if match:
                    num1, num2 = map(int, match.groups())
                    result += num1 * num2
    return result
    
if __name__ == "__main__":
    l = read_file("input.txt")
    print(f"Résulat de la partie 1 : {part1(l)}")
    print(f"Résulat de la partie 2 : {part2(l)}")
    