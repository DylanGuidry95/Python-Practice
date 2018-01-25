from a_star import A_Star
from node import Node
from graph import Graph

NEWGRAPH = Graph(5, 5)

NEWGRAPH.generate_nodes()

ALGO = A_Star(NEWGRAPH)

ALGO.set_start_node(NEWGRAPH.nodes[2])
ALGO.set_goal_node(NEWGRAPH.nodes[22])
ALGO.set_wall(NEWGRAPH.nodes[12])
ALGO.set_wall(NEWGRAPH.nodes[13])
ALGO.set_wall(NEWGRAPH.nodes[11])

if ALGO.start_up():
    GOAL = ALGO.update()
    while GOAL is None:
        GOAL = ALGO.update()

for node in ALGO.closed_list:
    print str(node.position[0]) + "," + str(node.position[1])