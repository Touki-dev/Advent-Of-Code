def read_file(file):
    with open(file, 'r') as file:
        lignes = file.read().split('\n\n')
        return [ligne.strip().split("\n") for ligne in lignes]

def operand_combo(operand, A, B, C):
    """Calcule la valeur d'un opérande combo."""
    if operand <= 3:
        return operand
    elif operand == 4:
        return A
    elif operand == 5:
        return B
    elif operand == 6:
        return C
    return 0  # Cas réservé, non utilisé

def part1(l):
    registers = {
        "A": l[0][0].split(": ")[1],
        "B": l[0][1].split(": ")[1],
        "C": l[0][2].split(": ")[1]
    }
    program = list(map(int, l[1][0].split(": ")[1]))
    output = []
    
    for i in range(len(0, program, 2)):
        opcode = program[i]
        operand = program[i+1]
        
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
        
        # Passer à l'instruction suivante (sauf pour jnz)
        pointer += 2

def part2(l):
    ...

if __name__ == "__main__":
    l = read_file("input.txt")
    print(f"Résulat de la partie 1 : {part1(l)}")
    print(f"Résulat de la partie 2 : {part2(l)}")