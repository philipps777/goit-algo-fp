import networkx as nx
import matplotlib.pyplot as plt
import heapq

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = [(0, start)]

    while unvisited:
        current_distance, current_vertex = heapq.heappop(unvisited)

        for neighbor in graph.neighbors(current_vertex):
            weight = graph.get_edge_data(
                current_vertex, neighbor).get('вага', 0)
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(unvisited, (distance, neighbor))

    return distances


G_berlin_metro = nx.DiGraph()

station_names = [
    "Alexanderplatz", "Brandenburger Tor", "Zoologischer Garten", "Potsdamer Platz",
    "Spittelmarkt", "Friedrichstraße", "Hackescher Markt", "Kurfürstendamm",
    "Wittenbergplatz", "Schönhauser Allee", "Schlesisches Tor", "Tierpark",
    "Frankfurter Allee", "Hermannplatz", "Märkisches Museum"
]
G_berlin_metro.add_nodes_from(station_names)
edges_with_distances = [
    ("Alexanderplatz", "Brandenburger Tor", {'вага': 3}),
    ("Brandenburger Tor", "Zoologischer Garten", {'вага': 4}),
    ("Zoologischer Garten", "Potsdamer Platz", {'вага': 5}),
    ("Potsdamer Platz", "Spittelmarkt", {'вага': 5}),
    ("Spittelmarkt", "Friedrichstraße", {'вага': 3}),
    ("Friedrichstraße", "Hackescher Markt", {'вага': 2}),
    ("Hackescher Markt", "Kurfürstendamm", {'вага': 6}),
    ("Kurfürstendamm", "Wittenbergplatz", {'вага': 4}),
    ("Wittenbergplatz", "Schönhauser Allee", {'вага': 7}),
    ("Schönhauser Allee", "Schlesisches Tor", {'вага': 8}),
    ("Schlesisches Tor", "Tierpark", {'вага': 5}),
    ("Tierpark", "Frankfurter Allee", {'вага': 3}),
    ("Frankfurter Allee", "Hermannplatz", {'вага': 6}),
    ("Hermannplatz", "Märkisches Museum", {'вага': 4}),
    ("Kurfürstendamm", "Alexanderplatz", {'вага': 24}),
    ("Potsdamer Platz", "Schönhauser Allee", {'вага': 37}),
    ("Friedrichstraße", "Schlesisches Tor", {'вага': 18}),
    ("Spittelmarkt", "Tierpark", {'вага': 35}),
    ("Kurfürstendamm", "Frankfurter Allee", {'вага': 23}),
    ("Frankfurter Allee", "Zoologischer Garten", {'вага': 16}),
    ("Hackescher Markt", "Märkisches Museum", {'вага': 44}),
]

G_berlin_metro.add_edges_from(edges_with_distances)

# Example usage of Dijkstra's algorithm on the Berlin metro graph
start_station = "Alexanderplatz"
shortest_distances = dijkstra(G_berlin_metro, start_station)

# Displaying the shortest distances from the start station
print(f"Shortest distances from {start_station}:")
for station, distance in shortest_distances.items():
    print(f"{station}: {distance}")

# Visualization of the graph
pos = nx.circular_layout(G_berlin_metro)
nx.draw(G_berlin_metro, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=8,
        font_color='black', font_weight='bold', edge_color='gray', width=1.5, font_family='Arial')

edge_labels = nx.get_edge_attributes(G_berlin_metro, 'вага')
nx.draw_networkx_edge_labels(
    G_berlin_metro, pos, edge_labels=edge_labels, font_color='red')

plt.show()

#
# import networkx as nx
# import matplotlib.pyplot as plt
# import heapq
#
# def dijkstra(graph, start):
#     distances = {vertex: float('infinity') for vertex in graph}
#     distances[start] = 0
#     unvisited = [(0, start)]
#
#     while unvisited:
#         current_distance, current_vertex = heapq.heappop(unvisited)
#
#         for neighbor, edge_data in graph[current_vertex].items():
#             weight = edge_data.get('вага', 0)
#             distance = current_distance + weight
#
#             if distance < distances[neighbor]:
#                 distances[neighbor] = distance
#                 heapq.heappush(unvisited, (distance, neighbor))
#
#     return distances
#
# # Створення графа
# G_berlin_metro = nx.DiGraph()
#
# station_names = [
#     "Alexanderplatz", "Brandenburger Tor", "Zoologischer Garten", "Potsdamer Platz",
#     "Spittelmarkt", "Friedrichstraße", "Hackescher Markt", "Kurfürstendamm",
#     "Wittenbergplatz", "Schönhauser Allee", "Schlesisches Tor", "Tierpark",
#     "Frankfurter Allee", "Hermannplatz", "Märkisches Museum"
# ]
# G_berlin_metro.add_nodes_from(station_names)
#
# edges_with_distances = [
#     ("Alexanderplatz", "Brandenburger Tor", {'вага': 3}),
#     ("Brandenburger Tor", "Zoologischer Garten", {'вага': 4}),
#     ("Zoologischer Garten", "Potsdamer Platz", {'вага': 5}),
#     ("Potsdamer Platz", "Spittelmarkt", {'вага': 5}),
#     ("Spittelmarkt", "Friedrichstraße", {'вага': 3}),
#     ("Friedrichstraße", "Hackescher Markt", {'вага': 2}),
#     ("Hackescher Markt", "Kurfürstendamm", {'вага': 6}),
#     ("Kurfürstendamm", "Wittenbergplatz", {'вага': 4}),
#     ("Wittenbergplatz", "Schönhauser Allee", {'вага': 7}),
#     ("Schönhauser Allee", "Schlesisches Tor", {'вага': 8}),
#     ("Schlesisches Tor", "Tierpark", {'вага': 5}),
#     ("Tierpark", "Frankfurter Allee", {'вага': 3}),
#     ("Frankfurter Allee", "Hermannplatz", {'вага': 6}),
#     ("Hermannplatz", "Märkisches Museum", {'вага': 4}),
#     ("Kurfürstendamm", "Alexanderplatz", {'вага': 24}),
#     ("Potsdamer Platz", "Schönhauser Allee", {'вага': 37}),
#     ("Friedrichstraße", "Schlesisches Tor", {'вага': 18}),
#     ("Spittelmarkt", "Tierpark", {'вага': 35}),
#     ("Kurfürstendamm", "Frankfurter Allee", {'вага': 23}),
#     ("Frankfurter Allee", "Zoologischer Garten", {'вага': 16}),
#     ("Hackescher Markt", "Märkisches Museum", {'вага': 44}),
# ]
#
# G_berlin_metro.add_edges_from(edges_with_distances)
#
# # Початкова станція для алгоритму
# start_station = "Alexanderplatz"
#
# # Застосування алгоритму Дейкстри
# shortest_distances = dijkstra(G_berlin_metro, start_station)
#
# # Виведення найкоротших відстаней
# print(f"Найкоротші відстані від {start_station}:")
# for station, distance in shortest_distances.items():
#     print(f"{station}: {distance}")
#
# # Візуалізація графа
# pos = nx.circular_layout(G_berlin_metro)
# nx.draw(G_berlin_metro, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=8,
#         font_color='black', font_weight='bold', edge_color='gray', width=1.5, font_family='Arial')
#
# edge_labels = nx.get_edge_attributes(G_berlin_metro, 'вага')
# nx.draw_networkx_edge_labels(
#     G_berlin_metro, pos, edge_labels=edge_labels, font_color='red')
#
# plt.show()


# import networkx as nx
# import matplotlib.pyplot as plt
#
#
# def print_table(distances, visited):
#     # Верхній рядок таблиці
#     print("{:<10} {:<10} {:<10}".format("Вершина", "Відстань", "Перевірено"))
#     print("-" * 30)
#
#
#     for vertex in distances:
#         distance = distances[vertex]
#         if distance == float('infinity'):
#             distance = "∞"
#         else:
#             distance = str(distance)
#
#         status = "Так" if vertex in visited else "Ні"
#         print("{:<10} {:<10} {:<10}".format(vertex, distance, status))
#     print("\n")
#
#
# def dijkstra(graph, start):
#     distances = {vertex: float('infinity') for vertex in graph}
#     distances[start] = 0
#     unvisited = list(graph.nodes)
#     visited = []
#
#     while unvisited:
#         current_vertex = min(unvisited, key=lambda vertex: distances[vertex])
#
#         if distances[current_vertex] == float('infinity'):
#             break
#
#         for neighbor in graph.neighbors(current_vertex):
#             weight = graph.get_edge_data(current_vertex, neighbor).get('вага', 0)
#             distance = distances[current_vertex] + weight
#             if distance < distances[neighbor]:
#                 distances[neighbor] = distance
#
#         visited.append(current_vertex)
#         unvisited.remove(current_vertex)
#
#
#         print_table(distances, visited)
#
#     return distances
#
#
#
# G_berlin_metro = nx.DiGraph()
#
# station_names = [
#     "Alexanderplatz", "Brandenburger Tor", "Zoologischer Garten", "Potsdamer Platz",
#     "Spittelmarkt", "Friedrichstraße", "Hackescher Markt", "Kurfürstendamm",
#     "Wittenbergplatz", "Schönhauser Allee", "Schlesisches Tor", "Tierpark",
#     "Frankfurter Allee", "Hermannplatz", "Märkisches Museum"
# ]
# G_berlin_metro.add_nodes_from(station_names)
# edges_with_distances = [
#         ("Alexanderplatz", "Brandenburger Tor", {'вага': 3}),
#         ("Brandenburger Tor", "Zoologischer Garten", {'вага': 4}),
#         ("Zoologischer Garten", "Potsdamer Platz", {'вага': 5}),
#         ("Potsdamer Platz", "Spittelmarkt", {'вага': 5}),
#         ("Spittelmarkt", "Friedrichstraße", {'вага': 3}),
#         ("Friedrichstraße", "Hackescher Markt", {'вага': 2}),
#         ("Hackescher Markt", "Kurfürstendamm", {'вага': 6}),
#         ("Kurfürstendamm", "Wittenbergplatz", {'вага': 4}),
#         ("Wittenbergplatz", "Schönhauser Allee", {'вага': 7}),
#         ("Schönhauser Allee", "Schlesisches Tor", {'вага': 8}),
#         ("Schlesisches Tor", "Tierpark", {'вага': 5}),
#         ("Tierpark", "Frankfurter Allee", {'вага': 3}),
#         ("Frankfurter Allee", "Hermannplatz", {'вага': 6}),
#         ("Hermannplatz", "Märkisches Museum", {'вага': 4}),
#         ("Kurfürstendamm", "Alexanderplatz", {'вага': 24}),
#         ("Potsdamer Platz", "Schönhauser Allee", {'вага': 37}),
#         ("Friedrichstraße", "Schlesisches Tor", {'вага': 18}),
#         ("Spittelmarkt", "Tierpark", {'вага': 35}),
#         ("Kurfürstendamm", "Frankfurter Allee", {'вага': 23}),
#         ("Frankfurter Allee", "Zoologischer Garten", {'вага': 16}),
#         ("Hackescher Markt", "Märkisches Museum", {'вага': 44}),
#     ]
#
# G_berlin_metro.add_edges_from(edges_with_distances)
# num_nodes = G_berlin_metro.number_of_nodes()
# num_edges = G_berlin_metro.number_of_edges()
#
# degrees = dict(G_berlin_metro.degree())
# degree_centrality = nx.degree_centrality(G_berlin_metro)
#
# print("Кількість вершин у графі: ", num_nodes)
# print("Кількість ребер у графі: ", num_edges)
# print("Ступінь вершин: ", degrees)
# print("Ступінь центральності вершин: ", degree_centrality)
#
#
# start_vertex = "Alexanderplatz"
# shortest_paths = {vertex: dijkstra(G_berlin_metro, vertex) for vertex in G_berlin_metro.nodes}
#
#
# pos = nx.circular_layout(G_berlin_metro)
# nx.draw(G_berlin_metro, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=8,
#         font_color='black', font_weight='bold', edge_color='gray', width=1.5, font_family='Arial')
#
# edge_labels = nx.get_edge_attributes(G_berlin_metro, 'вага')
# nx.draw_networkx_edge_labels(
#     G_berlin_metro, pos, edge_labels=edge_labels, font_color='red')
#
# plt.show()
