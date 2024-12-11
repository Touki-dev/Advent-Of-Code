from typing import List
from collections import Counter, defaultdict
from functools import lru_cache

def read_file(file):
    with open(file, 'r') as f:
        return list(int(num) for num in f.read().split())

@lru_cache(maxsize=None)
def process_single_stone(stone: int) -> List[int]:
    if stone == 0:
        return [1]
    elif len(str(stone)) % 2 == 0:
        str_stone = str(stone)
        left_half = int(str_stone[:len(str_stone)//2])
        right_half = int(str_stone[len(str_stone)//2:])
        return [left_half, right_half]
    else:
        return [stone * 2024]

def process_stones(stones: Counter) -> Counter:
    result = defaultdict(int)
    
    for stone, num in stones.items():
        processed = process_single_stone(stone)
        for processed_stone in processed:
            result[processed_stone] += num
    
    return Counter(result)

def part1(l):
    result = Counter(l)
    for _ in range(25):
        result = process_stones(result)
    return sum(result.values())

def part2(l):
    result = Counter(l)
    for _ in range(75):
        result = process_stones(result)
    return sum(result.values())

if __name__ == "__main__":
    l = read_file("input.txt")
    print(l)
    print(f"Résulat de la partie 1 : {part1(l)}")
    print(f"Résulat de la partie 2 : {part2(l)}")