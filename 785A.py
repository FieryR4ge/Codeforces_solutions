n = int(input())

edges = {
    "Icosahedron": 20,
    "Cube": 6,
    "Tetrahedron": 4,
    "Dodecahedron": 12,
    "Octahedron": 8
    }

edge_counter = 0

for i in range(n):
    edge_counter += edges[input()]

print(edge_counter)
