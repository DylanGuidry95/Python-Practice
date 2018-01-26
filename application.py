#pylint: disable=E1101
import pygame
from a_star import AStar
from graph import Graph
from node import Node

#pygame variables
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720

BACKGROUND_COLOR = (0, 0, 0)

#astar variables(not visuals)
GRAPH = Graph(10, 10)
GRAPH.generate_nodes()
ALGO = AStar(GRAPH)
ALGO.set_start_node(GRAPH.nodes[0])
ALGO.set_goal_node(GRAPH.nodes[99])

def main():
    '''Main functionality of the application'''
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill(BACKGROUND_COLOR)

    ALGO.start_up()

    while update():
        goal = None
        if goal is None:
            goal = ALGO.update()
        if goal is not None:
            current = goal
            while current != None:
                print str(current.position[0]) + "," + str(current.position[1])
                current = current.parent

        #Do not remove this line
        pygame.display.flip()

def update():
    '''Will return true as long as the QUIT event has not been invoked'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True


main()
