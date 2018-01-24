from a_star import A_Star
from node import Node
from graph import Graph

newGraph = Graph(2,2)

newGraph.generate_nodes()
newGraph.display_grid()


algo = A_Star(newGraph)

algo.set_start_node(newGraph.nodes[0])
algo.set_goal_node(newGraph.nodes[3])
algo.get_neighbors()