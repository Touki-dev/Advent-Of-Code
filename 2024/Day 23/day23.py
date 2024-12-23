def read_file(file):
    with open(file, 'r') as file:
        lignes = file.read().split('\n')
        return lignes

def parse_input(l):
    # Créer un graphe sous forme de dictionnaire
    graph = {}
    for line in l:
        a, b = line.split("-")
        if a not in graph:
            graph[a] = set()
        if b not in graph:
            graph[b] = set()
        graph[a].add(b)
        graph[b].add(a)
    return graph

def part1(l):
    def find_triangles(graph):
        triangles = set()
        for node in graph:
            neighbors = graph[node]
            for neighbor in neighbors:
                # Trouver les voisins communs entre le nœud et son voisin
                common_neighbors = neighbors.intersection(graph[neighbor])
                for cn in common_neighbors:
                    # Créer un triangle ordonné (pour éviter les doublons)
                    triangle = tuple(sorted([node, neighbor, cn]))
                    triangles.add(triangle)
        return triangles

    # Étapes de calcul
    graph = parse_input(l)
    triangles = find_triangles(graph)

    return len([triangle for triangle in triangles if any(comp[0] == "t" for comp in triangle)])

def part2(l):
    def parse_input_optimized(l):
        graph = {}
        for line in l:
            a, b = line.split("-")
            graph.setdefault(a, set()).add(b)
            graph.setdefault(b, set()).add(a)
        return graph

    def find_largest_clique_optimized(graph):
        # Trier les nœuds par degré décroissant
        sorted_nodes = sorted(graph.keys(), key=lambda x: len(graph[x]), reverse=True)
        largest_clique = set()

        for node in sorted_nodes:
            # Construire une clique autour du nœud actuel
            current_clique = {node}
            for neighbor in graph[node]:
                if all(neighbor in graph[other] for other in current_clique):
                    current_clique.add(neighbor)
            # Mettre à jour si cette clique est plus grande
            if len(current_clique) > len(largest_clique):
                largest_clique = current_clique

        return largest_clique

    def generate_password_optimized(clique):
        return ",".join(sorted(clique))

    # Étapes de calcul optimisées
    graph = parse_input_optimized(l)
    largest_clique = find_largest_clique_optimized(graph)
    password = generate_password_optimized(largest_clique)

    return largest_clique, password

if __name__ == "__main__":
    l = read_file("input.txt")
    print(f"Résulat de la partie 1 : {part1(l)}")
    print(f"Résulat de la partie 2 : {part2(l)}")