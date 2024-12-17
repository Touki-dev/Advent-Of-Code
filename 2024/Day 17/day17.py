def read_file(file):
    with open(file, 'r') as file:
        lignes = file.read().split('\n\n')
        return [ligne.strip().split("\n") for ligne in lignes]

def operand_combo(operand, A, B, C):
    if operand <= 3:
        return operand
    elif operand == 4:
        return A
    elif operand == 5:
        return B
    elif operand == 6:
        return C
    return 0

def run_program(program, registres):
    A,B,C = registres
    output = []
    pointer = 0
    
    while pointer < len(program):
        opcode = program[pointer]
        operand = program[pointer+1]
        
        if opcode == 0:  # adv
            denominator = 2 ** operand_combo(operand, A, B, C)
            A = A // denominator if denominator != 0 else 0
        
        elif opcode == 1:  # bxl
            B ^= operand
        
        elif opcode == 2:  # bst
            B = operand_combo(operand, A, B, C) % 8
        
        elif opcode == 3:  # jnz
            if A != 0:
                pointer = operand
                continue
        
        elif opcode == 4:  # bxc
            B ^= C
        
        elif opcode == 5:  # out
            output.append(operand_combo(operand, A, B, C) % 8)
        
        elif opcode == 6:  # bdv
            denominator = 2 ** operand_combo(operand, A, B, C)
            B = A // denominator if denominator != 0 else 0
        
        elif opcode == 7:  # cdv
            denominator = 2 ** operand_combo(operand, A, B, C)
            C = A // denominator if denominator != 0 else 0
            
        pointer += 2
        
    return output

def part1(l):
    A = int(l[0][0].split(": ")[1])
    program = list(map(int, l[1][0].split(": ")[1].split(',')))
    output = run_program(program, [A,0,0])
    return ",".join(list(map(str, output)))

def part2(l):
    program = list(map(int, l[1][0].split(": ")[1].split(',')))
    A = sum(7 * 8**i for i in range(len(program) - 1)) + 1

    while True:
        result = run_program(program, [A,0,0])

        if len(result) > len(program):
            raise ValueError("Trop long !")

        if result == program:
            return A
        add = 0
        for i in range(len(result) - 1, -1, -1):
            if result[i] != program[i]:
                add = 8**i
                A += add
                break

if __name__ == "__main__":
    l = read_file("input.txt")
    print(f"Résulat de la partie 1 : {part1(l)}")
    print(f"Résulat de la partie 2 : {part2(l)}")
