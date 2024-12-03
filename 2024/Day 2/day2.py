INPUT = open("input.txt", "r")
INPUT = INPUT.read().split('\n')

def testDifference(ligne):
    for j in range(1, len(ligne)):
        if int(ligne[j]) not in range(int(ligne[j-1])-3, int(ligne[j-1])+4):
            return False
    return True

def testAugment(ligne):
    if int(ligne[0]) - int(ligne[1]) < 0:
        sens = True
    elif int(ligne[0]) - int(ligne[1]) > 0:
        sens = False
    else:
        return False
    for j in range(1, len(ligne)):
        if int(ligne[j-1]) - int(ligne[j]) < 0:
            new_sens = True
        elif int(ligne[j-1]) - int(ligne[j]) > 0:
            new_sens = False
        else:
            return False
        
        if sens != new_sens:
            return False
    
    return True

def testPart1(ligne):
    if testDifference(ligne) and testAugment(ligne):
        return 1
    return 0

def testPart2(ligne):
    if testDifference(ligne) and testAugment(ligne):
        return 1
    for j in range(len(ligne)):
        new_ligne = list(ligne)
        new_ligne.pop(j)
        if testDifference(new_ligne) and testAugment(new_ligne):
            return 1
    return 0

if __name__ == "__main__":
    count = [0, 0]
    for i, ligne in enumerate(INPUT):
        ligne = ligne.split(' ')
        count[0] += testPart1(ligne)
        count[1] += testPart2(ligne)
        
    print(f"Résulat de la partie 1 : {count[0]}")
    print(f"Résulat de la partie 2 : {count[1]}")