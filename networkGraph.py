# Richard Taylor - Network Graph Builder - using Pyvis
from pyvis.network import Network
import csv
import random

# Settings for users to change
directed = False
bgcolor = "white"
font_color = "black"
fileName = input("Filename: ")
dir = input("Directed? [y/n]: ")
if dir == "y":
    directed = True


# Declaring Graph Object
net = Network(notebook=True,
              cdn_resources="local",
              directed=directed,
              bgcolor=bgcolor,
              font_color=font_color
              )

"""
Colour generator - takes in a colour and outputs a shade close to that colour
"""


def random_hex_color(colour):
    # @TODO Add more colours
    colours = {
        # blue
        "1": [0, 120, 100, 220, 210, 255],
        # orange
        "2": [245, 255, 100, 180, 0, 10],
        # green
        "3": [0, 60, 110, 255, 0, 70],
        # red
        "4": [180, 255, 0, 60, 0, 90]
    }
    red = random.randint(colours[colour][0], colours[colour][1])
    green = random.randint(colours[colour][2], colours[colour][3])
    blue = random.randint(colours[colour][4], colours[colour][5])
    return "#{0:02x}{1:02x}{2:02x}".format(red, green, blue)


"""
Read in csv file and populate the graph

"""
with open(fileName, 'r') as file:
    csvReader = csv.reader(file)

    listNodes = []
    count = True

    for row in csvReader:
        width = 0.1
        if row[2] != "":
            width = row[2]

        if count:
            count = False
            continue
        if row[0][1:] not in listNodes:
            listNodes.append(row[0][1:])
            net.add_node(listNodes.index(
                row[0][1:]), label=row[0][1:], physics=False, color=random_hex_color(row[0][0]))
        if row[1][1:] not in listNodes:
            listNodes.append(row[1][1:])
            net.add_node(listNodes.index(
                row[1][1:]), label=row[1][1:], physics=False, color=random_hex_color(row[1][0]))

        net.add_edge(listNodes.index(row[0][1:]),
                     listNodes.index(row[1][1:]), width=width, smooth=False, color="black")

"""
Resize nodes
"""
for node in net.nodes:
    edges = len(net.get_adj_list()[node['id']])
    node['size'] = edges * 4 + 1 + directed * 3

# Draw Graph
net.show("nodes.html")

print("Success! - Check this folder for HTML file!")
