# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

def search(problem, fringe):
    initial_state = problem.getStartState()
    initial_actions = []
    initial_candidate = (initial_state, initial_actions)
    fringe.push(initial_candidate)
    closed_set = set()
    while not fringe.isEmpty():
        candidate = fringe.pop()
        state, actions = candidate
        if problem.isGoalState(state):
            return actions
        if state not in closed_set:
            closed_set.add(state)
            candidate_successors = problem.getSuccessors(state)
            candidate_successors = filter(lambda x: x[0] not in closed_set, candidate_successors)
            candidate_successors = map(lambda x: (x[0], actions + [x[1]]), candidate_successors)
            for candidate in candidate_successors:
                fringe.push(candidate)

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """

    # print "Start:", problem.getStartState()
    # print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    # print "Start's successors:", problem.getSuccessors(problem.getStartState())
    # print "-------------_FIN-------------------"


    # Implementamos el dfs pero notamos que ya existia una funcion simple para buscar
    # listaNodos = util.Stack()
    # listaNodos.push((problem.getStartState(),[],0))
    # visitados = set()

    # while not listaNodos.isEmpty():
    #     actual, direccion, costo = listaNodos.pop()
    #     if actual not in visitados:    
    #         visitados.add(actual)
    #         if problem.isGoalState(actual):
    #             return direccion
    #         else:
    #             for i in problem.getSuccessors(actual):
    #                 if i[0] not in visitados:
    #                     listaNodos.push((i[0],direccion + [i[1]],i[2] + costo))
    return search(problem, util.Stack())

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    # Implementamos el bfs pero notamos que ya existia una funcion simple para buscar
    # listaNodos = util.Queue()
    # listaNodos.push((problem.getStartState(),[],0))
    # visitados = set()

    # while not listaNodos.isEmpty():
    #     actual, direccion, costo = listaNodos.pop()
    #     if actual not in visitados:
    #         visitados.add(actual)
    #         if problem.isGoalState(actual):
    #             return direccion
    #         else:
    #             for i in problem.getSuccessors(actual):
    #                 if i[0] not in visitados:
    #                     listaNodos.push((i[0],direccion + [i[1]],i[2] + costo))
    return search(problem, util.Queue())

def uniformCostSearch(problem):
    "Search the node of least total cost first."

    # Podriamos modificar la funcion search para implementar este caso y el A* pero no nos parecio util
    listaNodos = util.PriorityQueue()
    listaNodos.push((problem.getStartState(),[],0),0)
    visitados = set()

    while not listaNodos.isEmpty():
        actual, direccion,costo = listaNodos.pop()
        if actual not in visitados:    
            visitados.add(actual)
            if problem.isGoalState(actual):
                return direccion
            else:
                for i in problem.getSuccessors(actual):
                    if i[0] not in visitados:
                        listaNodos.push((i[0],direccion + [i[1]], i[2] + costo),i[2] + costo)

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    listaNodos = util.PriorityQueue()
    start = problem.getStartState()
    listaNodos.push((start,[],0),heuristic(start,problem))
    visitados = set()

    while not listaNodos.isEmpty():
        actual, direccion,costo = listaNodos.pop()
        if actual not in visitados:
            visitados.add(actual)
            if problem.isGoalState(actual):
                return direccion
            else:
                for i in problem.getSuccessors(actual):
                    if i[0] not in visitados:
                        consistente = heuristic(i[0],problem) + 1 >= heuristic(actual,problem)
                        assert(consistente)
                        listaNodos.push((i[0],direccion + [i[1]], i[2] + costo),i[2] + costo + heuristic(i[0],problem))



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
