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
    internal = []
    "initialize the search graph using the initial state of problem"
    frontier.push((problem.getStartState(), []))
    "graph-search(problem, strategy) returns a solution, or failure"
    while not frontier.isEmpty():
        "choose a frontier node for expansion according to strategy"
        pos = frontier.pop()
        node = pos[0]
        path = pos[1]
        "if the node contains a goal state then return the corresponding solution"
        if problem.isGoalState(node):
            return path
        "else expand the node and add the resulting nodes to the search tree"
        if node not in internal:
            internal.append(node)
            # get each new frontier node and push them onto the stack as a tuple of the node and path to said node
            for newfrontier in problem.getSuccessors(node):
                if newfrontier not in internal:
                    nfnode = newfrontier[0]
                    cpath = path + [newfrontier[1]]
                    frontier.push((nfnode, cpath))
    "if there are no candidates for expansion then return failure"
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
    internal = []
    "initialize the search graph using the initial state of problem"
    frontier.push((problem.getStartState(), [])) 
    "graph-search(problem, strategy) returns a solution, or failure"
    while not frontier.isEmpty():
        "choose a frontier node for expansion according to strategy"
        pos = frontier.pop()
        node = pos[0]
        path = pos[1]
        "if the node contains a goal state then return the corresponding solution"
        if problem.isGoalState(node):
            return path
        "else expand the node and add the resulting nodes to the search tree"
        if node not in internal:
            internal.append(node)
            # get each new frontier node and push them onto the queue as a tuple of the node and path to said node
            for newfrontier in problem.getSuccessors(node):
                if newfrontier not in internal:
                    nfnode = newfrontier[0]
                    cpath = path + [newfrontier[1]]
                    frontier.push((nfnode, cpath))  
    "if there are no candidates for expansion then return failure"
    print("Failure! BFS could not find a goal!")
    return[]

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    
    """The overarching structure of this code for UCS remains the same as DFS and BFS, but with
       a handful of significant changes. First, frontier has now become a PriorityQueue data structure
       in place of a Stack or Queue, owing to UCS' focus on uniform priority popping of queue notes.
       Second, the start state has been given a priority of 0 for its initial push, complying with
       PriorityQueue syntax. Third, nodes are now popped from frontier based off the lowest priority,
       while storing said priority for use in calculating the priority of new frontier nodes. Fourth,
       the same field is stored for each new frontier node, separate from the previously mentioned
       priority. Finally, each node pushed now stores a tuple of the node, its cumulative path, and
       its cumulative cost, while storing said cumulative cost redundantly in a second field outside
       the tuple for priorityqueue popping. This tuple is used in the next iteration of the while loop
       for whichever node is popped. As far as handling costs priority for which to pop next, that entire
       process is automated by the priorityqueue data structure itself via a chosen popping of the element
       with the lowest priority."""

    "initialize stack (LIFO) for expandable nodes and set (unique objects) for internal nodes"
    frontier = util.PriorityQueue()
    internal = []
    "initialize the search graph using the initial state of problem"
    frontier.push((problem.getStartState(), [], 0), 0) # start node is priority 0, already visited 
    "graph-search(problem, strategy) returns a solution, or failure"
    while not frontier.isEmpty():
        "choose a frontier node for expansion according to strategy"
        pos = frontier.pop() # pop nodes based on their priority
        node = pos[0]
        path = pos[1]
        prio = pos[2]
        "if the node contains a goal state then return the corresponding solution"
        if problem.isGoalState(node):
            return path
        "else expand the node and add the resulting nodes to the search tree"
        if node not in internal:
            internal.append(node)
            for newfrontier in problem.getSuccessors(node):
                if newfrontier not in internal:
                    nfnode = newfrontier[0]
                    cpath = path + [newfrontier[1]]
                    cprio = newfrontier[2] + prio
                    frontier.push((nfnode, cpath, cprio), cprio)
    "if there are no candidates for expansion then return failure"
    print("Failure! UCS could not find a goal!")
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
    
    """The structure of this code most closely aligns with the previous UCS function, but there
       is a single key difference in the heuristic calculation being appended to the priority of
       newly pushed nodes in each iteration. This is the only thing that functionally separates
       A* from UCS as a coded algorithm."""
    
    "initialize stack (LIFO) for expandable nodes and set (unique objects) for internal nodes"
    frontier = util.PriorityQueue()
    internal = []
    "initialize the search graph using the initial state of problem"
    frontier.push((problem.getStartState(), [], 0), 0) # start node is priority 0, already visited 
    "graph-search(problem, strategy) returns a solution, or failure"
    while not frontier.isEmpty():
        "choose a frontier node for expansion according to strategy"
        pos = frontier.pop() # pop nodes based on their priority
        node = pos[0]
        path = pos[1]
        prio = pos[2]
        "if the node contains a goal state then return the corresponding solution"
        if problem.isGoalState(node):
            return path
        "else expand the node and add the resulting nodes to the search tree"
        if node not in internal:
            internal.append(node)
            for newfrontier in problem.getSuccessors(node):
                if newfrontier not in internal:
                    nfnode = newfrontier[0]
                    cpath = path + [newfrontier[1]]
                    cprio = newfrontier[2] + prio
                    #print(heuristic(nfnode, problem))
                    frontier.push((nfnode, cpath, cprio), cprio + heuristic(nfnode, problem))
    "if there are no candidates for expansion then return failure"
    print("Failure! A* could not find a goal!")
    return[]
    


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch