import networkx as nx
import matplotlib.pyplot as plt
import csv

G = nx.Graph()

with open('links.csv', 'r') as file:
    csvReader = csv.reader(file)
    listNodes = []

    for row in csvReader:
        if row[0] not in listNodes:
            G.add_node(row[0])
        if row[1] not in listNodes:
            G.add_node(row[1])
        G.add_edge(row[0], row[1])

# Draw the graph
nx.draw(G, with_labels=True)

# Show the graph
plt.show()
