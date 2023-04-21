# Richard Taylor - Network Graph Builder - using Pyvis
from pyvis.network import Network
import csv
import random

net = Network(notebook=True,
              cdn_resources="remote",
              # directed=True,
              bgcolor="white",
              font_color="black"
              )


def random_hex_color(color):
    # @TODO Python dict
    red = random.randint(0, 150)
    green = random.randint(100, 220)
    blue = random.randint(210, 255)
    return "#{0:02x}{1:02x}{2:02x}".format(red, green, blue)


#fileName = input("Enter a filename: ")
fileName = "links (version 1).csv"
with open(fileName, 'r') as file:
    csvReader = csv.reader(file)

    listNodes = []
    count = True
    for row in csvReader:
        if count:
            count = False
            continue
        if row[0] not in listNodes:
            listNodes.append(row[0])
            net.add_node(listNodes.index(
                row[0]), label=row[0], physics=False, color=random_hex_color("blue"))
        if row[1] not in listNodes:
            listNodes.append(row[1])
            net.add_node(listNodes.index(
                row[1]), label=row[1], physics=False, color=random_hex_color("blue"))

        net.add_edge(listNodes.index(row[0]),
                     listNodes.index(row[1]), width=0.1, smooth=False, color="black")


for node in net.nodes:
    edges = len(net.get_adj_list()[node['id']])
    node['size'] = edges * 4 + 1
    print(node["label"], "has", edges, "edges")

net.set_options("""
    var options = {
      "directed": true
    }
""")

print(random_hex_color("catergory"))
# net.show_buttons(filter_=['physics'])
net.show("nodes.html")
