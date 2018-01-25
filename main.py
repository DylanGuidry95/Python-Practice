from a_star import A_Star
from node import Node
from graph import Graph

NEWGRAPH = Graph(5, 5)

NEWGRAPH.generate_nodes()

ALGO = A_Star(NEWGRAPH)

ALGO.set_start_node(NEWGRAPH.nodes[0])
ALGO.set_goal_node(NEWGRAPH.nodes[24])

if ALGO.start_up:
    while ALGO.update() is None:
        print "Algoritm running"
