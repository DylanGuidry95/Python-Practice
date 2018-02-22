import pygame
from AStar_App import AStar_App
from A_Star.a_star import AStar
from A_Star.graph import Graph

GRAPH = Graph(10,10)
GRAPH.generate_nodes()
ASTAR = AStar(GRAPH)