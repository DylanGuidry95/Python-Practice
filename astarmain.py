from a_star import AStar
from node import Node
from graph import Graph

NEWGRAPH = Graph(5, 5)

NEWGRAPH.generate_nodes()

ALGO = AStar(NEWGRAPH)

ALGO.set_start_node(NEWGRAPH.nodes[2])
ALGO.set_goal_node(NEWGRAPH.nodes[22])
ALGO.set_wall(NEWGRAPH.nodes[12])
ALGO.set_wall(NEWGRAPH.nodes[13])
ALGO.set_wall(NEWGRAPH.nodes[11])

if ALGO.start_up():
    GOAL = ALGO.update()
    while GOAL is None:
        GOAL = ALGO.update()

CURRENT = GOAL
while CURRENT != None:
    print str(CURRENT.position[0]) + "," + str(CURRENT.position[1])
    CURRENT = CURRENT.parent
