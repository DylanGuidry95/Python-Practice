import pygame
from AStar_App import AStar_App
from A_Star.a_star import AStar
from A_Star.graph import Graph
from astartest import *

GRAPH = Graph(10,10)
ASTAR = AStar(GRAPH)

testfunc(ASTAR.update)

APP = AStar_App("Test", (1080, 720), (5, 5))
APP.start()

APP.update()
