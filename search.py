# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
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
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]
# class for search algorithm
class SearchAlgorithm:
    def __init__(self, dataStructure):
        # Use a datastructure eg stack , queue etc,to explore node
        self.dataStructure = dataStructure
        # Make an empty list of explored nodes
        self.visited_nodes = []
        # Make an empty list of actions
        self.action = []


    def Searching(self,problem):
        # Place the starting point in the stack or queue depending on datastructure
        self.dataStructure .push((problem.getStartState(), self.action))
        while self.dataStructure :
            node, actions = self.dataStructure .pop()
            if not node in self.visited_nodes :
                self.visited_nodes.append(node)
                if problem.isGoalState(node):
                    return actions
                for successor in problem.getSuccessors(node):
                    coordinate, direction, cost = successor
                    nextActions = actions + [direction]
                    self.dataStructure .push((coordinate, nextActions))
        return []


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    # creating an instance of a stack and pass as argument to searchAlgorithm class
    search = SearchAlgorithm(util.Stack() )
    x = search.Searching(problem)
    return x
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # creating an instance of a Queue and pass as argument to searchAlgorithm class
    search = SearchAlgorithm(util.Queue())
    x =  search.Searching(problem)
    return x
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # an instance of PriorityQueue
    priortyQueue = util.PriorityQueue()
    # An empty list of nodes visited
    visited_nodes= []
    # An empty list of actions
    action = []
    # Placing the starting point in the queue
    priortyQueue .push((problem.getStartState(), action), problem)
    while priortyQueue :
        node, actions = priortyQueue.pop()
        if not node in visited_nodes :
            visited_nodes.append(node)
            if problem.isGoalState(node):
                return actions
            for successor in problem.getSuccessors(node):
                coordinate, direction, cost = successor
                nextActions = actions + [direction]
                nextCost = problem.getCostOfActions(nextActions)
                priortyQueue.push((coordinate, nextActions), nextCost)
    return []


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
