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

def depthFirstSearch(problem: SearchProblem):
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
    
    "initialize stack (LIFO) for expandable nodes and set (unique objects) for internal nodes"
    frontier = util.Stack()
    internal = set()
    "initialize the search graph using the initial state of problem"
    frontier.push((problem.getStartState(), [])) 
    print(internal)
    "graph-search(problem, strategy) returns a solution, or failure"
    while not frontier.isEmpty():
        "choose a frontier node for expansion according to strategy"
        node, path = frontier.pop()
        "if the node contains a goal state then return the corresponding solution"
        if problem.isGoalState(node):
            print(internal)
            return path
        "else expand the node and add the resulting nodes to the search tree"
        print(node)
        if node not in internal:
            internal.add(node)
            for newfrontier, move, _ in problem.getSuccessors(node):
                if newfrontier not in internal:
                    frontier.push((newfrontier, path + [move]))  
    "if there are no candidates for expansion then return failure"
    print(internal)
    print("Failure! DFS could not find a goal!")
    return[]

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    """There is quite literally a single difference between this code for BFS and and the Q1 code for DFS,
       and that is the change from a stack to a queue for the data structure of frontier. Every other line
       of code is exactly the same but seems to be able to pass all tests for Q2."""

    "initialize stack (LIFO) for expandable nodes and set (unique objects) for internal nodes"
    frontier = util.Queue()
    internal = set()
    "initialize the search graph using the initial state of problem"
    frontier.push((problem.getStartState(), [])) 
    print(internal)
    "graph-search(problem, strategy) returns a solution, or failure"
    while not frontier.isEmpty():
        "choose a frontier node for expansion according to strategy"
        node, path = frontier.pop()
        "if the node contains a goal state then return the corresponding solution"
        if problem.isGoalState(node):
            print(internal)
            return path
        "else expand the node and add the resulting nodes to the search tree"
        print(node)
        if node not in internal:
            internal.add(node)
            for newfrontier, move, _ in problem.getSuccessors(node):
                if newfrontier not in internal:
                    frontier.push((newfrontier, path + [move]))  
    "if there are no candidates for expansion then return failure"
    print(internal)
    print("Failure! DFS could not find a goal!")
    return[]

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    
    """The overarching structure of this code for UCS remains the same as DFS and BFS, but with
       a handful of significant changes. First, frontier has now become a PriorityQueue data structure
       in place of a Stack or Queue, owing to UCS' focus on uniform priority popping of queue notes.
       """

    "initialize stack (LIFO) for expandable nodes and set (unique objects) for internal nodes"
    frontier = util.PriorityQueue()
    internal = set()
    "initialize the search graph using the initial state of problem"
    frontier.push((problem.getStartState(), [], 0), 0) # start node is priority 0, already visited 
    "graph-search(problem, strategy) returns a solution, or failure"
    while not frontier.isEmpty():
        "choose a frontier node for expansion according to strategy"
        node, path, prio = frontier.pop()
        "if the node contains a goal state then return the corresponding solution"
        if problem.isGoalState(node):
            return path
        "else expand the node and add the resulting nodes to the search tree"
        if node not in internal:
            internal.add(node)
            for newfrontier in problem.getSuccessors(node): # move and _ were giving a "string index out of range" error, so I removed them
                if newfrontier not in internal:
                    frontier.push((newfrontier[0], path + [newfrontier[1]], newfrontier[2] + prio), newfrontier[2] + prio)
    "if there are no candidates for expansion then return failure"
    print("Failure! DFS could not find a goal!")
    return[]

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
