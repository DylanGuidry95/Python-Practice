from a_star import A_Star
from node import Node
from graph import Graph

NEWGRAPH = Graph(2, 2)

NEWGRAPH.generate_nodes()
NEWGRAPH.display_grid()


ALGO = A_Star(NEWGRAPH)

ALGO.set_start_node(NEWGRAPH.nodes[0])
ALGO.set_goal_node(NEWGRAPH.nodes[3])
ALGO.get_neighbors()
