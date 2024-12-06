import networkx as nx
def read_file(file):
    with open(file, 'r') as file:
        return [(i[0], list(i[1].split())) for i in (line.split(': ') for line in file)]

l = read_file("input.txt")

# Chargement du graphe avec les listes de connexions
GRAPHE = nx.Graph()
edges = [(i[0], j) for i in l for j in i[1]]
GRAPHE.add_edges_from(edges)

# Trouver une coupe minimale, surement de 3 arêtes
print("Coupe...")
cut_set = nx.minimum_edge_cut(GRAPHE)

# Afficher les arêtes dans la coupe
print("Edges in the Min-Cut:", cut_set)

# Supprimer les arêtes de la coupe
GRAPHE.remove_edges_from(cut_set)

# Trouver les composantes connectées
components = list(nx.connected_components(GRAPHE))
print("produit of Components", len(components[0]) * len(components[1]))