import pygame
from AStar_App import AStar_App
from A_Star.a_star import AStar
from A_Star.graph import Graph

GRAPH = Graph(10,10)
GRAPH.generate_nodes()
ASTAR = AStar(GRAPH)


def shuffle():
    '''shuffle some graph'''
    import random
    ranstart = random.randrange(0, 99)
    rangoal = random.randrange(0, 99)
    start = GRAPH[ranstart]
    goal = GRAPH[rangoal]
    for i in GRAPH:
        i.walkable = True
        i.parent = None
    blockers = []
    numblockers = random.randrange(0, 25)
    for i in range(numblockers):
        blockers.append(random.randrange(0, 99))
    copygraph = list(GRAPH)
    for i in blockers:
        copygraph[i].walkable = False
    result = ASTAR(start, goal, copygraph)
    return [start, goal, blockers, result]

def testfunc(astarfunc):
    '''test astar func'''
    test = shuffle()
    start = test[0]
    goal = test[1]
    unwalkable = test[2]
    expected = test[3]
    copygraph = list(GRAPH)
    for i in unwalkable:
        copygraph[i].walkable = False

    result = astarfunc(start, goal, copygraph)

    expectedres = []
    for i in expected:
        expectedres.append(int(i.guid))

    actualres = []
    for i in result:
        actualres.append(int(i.guid))
    line1 = str.format(
        'start::{0} goal::{1} unwalkables::{2}\n', start, goal, unwalkable)
    line2 = str.format('[[{0}], [{1}], {2}] \n', int(
        start.guid), int(goal.guid), unwalkable)
    line3 = str.format(
        'expected result {0} \nactual   result {1}\n', expectedres, actualres)
    if actualres == expectedres:
        print '========PASS TEST========='
    else:
        print '!!!!!!!!FAIL TEST!!!!!!!!!'

    print line1, line2, line3
    return actualres == expectedres

testfunc(ASTAR.update)