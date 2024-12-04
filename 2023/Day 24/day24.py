def read_file(file):
    with open(file, 'r') as file:
        return [(tuple(map(int, i[0].split(', '))), tuple(map(int, i[1].split(', ')))) for i in (line.split(' @ ') for line in file)]

def part1(l, zoneTest):
    hailstones = []
    for hs in l:
        # paramètre de l'equation y = mx+p
        m = hs[1][1] / hs[1][0]
        p = hs[0][1] - m * hs[0][0]
        hailstones.append({ "m": m, "p": p, "px": hs[0][0], "py": hs[0][1], "vx": hs[1][0], "vy": hs[1][1] })
      
    total = 0
    for i, hs1 in enumerate(hailstones):
        for hs2 in hailstones[:i]:
            m1, p1, m2, p2 = hs1["m"], hs1["p"], hs2["m"], hs2["p"]
            if m1 != m2:
                x = (p2 - p1)/(m1 - m2)
                y = m1*x + p1
                
                if (zoneTest[0] <= x <= zoneTest[1]) and (zoneTest[0] <= y <= zoneTest[1]):
                    if all((x - hs["px"]) * hs["vx"] >= 0 and (y - hs["py"]) * hs["vy"] >= 0 for hs in (hs1, hs2)):
                        total += 1
    
    return total

if __name__ == "__main__":
    l = read_file("input.txt")
    zoneTest = (200000000000000, 400000000000000)
    print(f"Résulat de la partie 1 : {part1(l, zoneTest)}")
    
    # print(f"Résulat de la partie 2 : {part2(l)}")