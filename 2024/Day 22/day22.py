from itertools import product
from tqdm import tqdm

def read_file(file):
    with open(file, 'r') as file:
        lignes = file.read().split('\n')
        return lignes


def part1(l):
    def generate_prices_and_changes(initial_secret):
        MODULO = 2**24
        secret = initial_secret
        prices = []
        changes = []

        # Generate 2000 secret numbers and prices
        for _ in range(2001):  # 2000 changes => 2001 prices
            price = secret % 10
            prices.append(price)
            secret = (secret ^ (secret * 64)) % MODULO
            secret = (secret ^ (secret // 32)) % MODULO
            secret = (secret ^ (secret * 2048)) % MODULO

        # Compute changes in prices
        for i in range(1, len(prices)):
            changes.append(prices[i] - prices[i - 1])
        
        return prices, changes
    
    def find_best_sequence(initial_secrets):
        

        # Generate all possible sequences of 4 changes
        possible_sequences = list(product(range(-9, 10), repeat=4))
        max_bananas = 0
        best_sequence = None

        # Analyze each sequence
        for sequence in possible_sequences:
            total_bananas = 0
            
            for secret in initial_secrets:
                _, changes = generate_prices_and_changes(secret)
                
                # Search for the sequence in the changes
                for i in range(len(changes) - 3):
                    if tuple(changes[i:i+4]) == sequence:
                        total_bananas += (changes[i + 4] + changes[0])
                        break

            # Check if this sequence is the best so far
            if total_bananas > max_bananas:
                max_bananas = total_bananas
                best_sequence = sequence

        return best_sequence, max_bananas
    initial_secrets = list(map(int, l))

    # Find the best sequence and maximum bananas
    return find_best_sequence(initial_secrets)

def part2(l):
    ...

if __name__ == "__main__":
    l = read_file("input.txt")
    print(f"Résulat de la partie 1 : {part1(l)}")
    print(f"Résulat de la partie 2 : {part2(l)}")