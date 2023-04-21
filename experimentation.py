from pyvis.network import Network

# create a Network object
net = Network(height="750px", width="100%",
              bgcolor="#222222", font_color="white")

# add nodes
net.add_node(1, label="Node 1", color="#FF0000", size=10)
net.add_node(2, label="Node 2", color="#00FF00", size=10)
net.add_node(3, label="Node 3", color="#0000FF", size=10)

# add edges
net.add_edge(1, 2, color="#FFFFFF")
net.add_edge(2, 3, color="#FFFFFF")
net.add_edge(3, 1, color="#FFFFFF")

# get the number of edges for each node
edges = net.get_adj_list()
for node_id in edges:
    num_edges = len(edges[node_id])
    print(f"Node {node_id} has {num_edges} edges")

# show the network graph
net.show("example.html")
