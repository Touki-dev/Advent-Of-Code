import networkx as nx
def read_file(file):
    with open(file, 'r') as file:
        return [(i[0], list(i[1].split())) for i in (line.split(': ') for line in file)]

l = read_file("input.txt")
# Chargement du graphe (liste d'arêtes par exemple)
G = nx.Graph()
edges = [(i[0], j) for i in l for j in i[1]]
G.add_edges_from(edges)

# Trouver une coupe minimale
cut_set = nx.minimum_edge_cut(G)

# Afficher les arêtes dans la coupe
print("Edges in the Min-Cut:", cut_set)

# Supprimer les arêtes de la coupe
G.remove_edges_from(cut_set)

# Trouver les composantes connectées
components = list(nx.connected_components(G))
print("produit of Components", len(components[0]) * len(components[1]))
