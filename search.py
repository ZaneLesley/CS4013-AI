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

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def chooseSearch(choice=0, problem=SearchProblem, heuristic=nullHeuristic):

    """This implementation relies entirely on chooseSearch to generically handle redundant lines
        of code common between each search algorithm while dynamically choosing specific operations
        based on the search algorithm the function is called with. This is accomplished using a blend
        of if-else statements and ternary operators (which are essentially inline if-else shortcuts). 
        The general path this function takes is equivalent to the lecture pseudocode for search tree 
        algorithms."""

    "initialize set (unique objects) for internal nodes and data structure for expandable nodes"
    internal = set()
    frontier = (util.Stack() if choice == 0 else
                util.Queue() if choice == 1 else
                util.PriorityQueue() if choice == 2 or choice == 3 else
                util.Stack())
    "initialize the search graph using the initial state of problem"
    if choice == 2 or choice == 3:
        frontier.push((problem.getStartState(), [], 0), 0)
    else:
        frontier.push((problem.getStartState(), []))
    "graph-search(problem, strategy) returns a solution, or failure"
    while not frontier.isEmpty():
        "choose a frontier node for expansion according to strategy"
        pos = frontier.pop()
        node = pos[0]
        path = pos[1]
        prio = (pos[2] if choice == 2 or choice == 3 else
                0)
        
        "if the node contains a goal state then return the corresponding solution"
        if problem.isGoalState(node):
            return path
        "else expand the node and add the resulting nodes to the search tree"
        if node not in internal:
            internal.add(node)
            for newfrontier in problem.getSuccessors(node):
                if newfrontier not in internal:
                    nfnode = newfrontier[0]
                    cpath = path + [newfrontier[1]]
                    cprio = ((newfrontier[2] + prio) if choice == 2 or choice == 3 else
                            0)
                    if choice == 2:
                        frontier.push((nfnode, cpath, cprio), cprio)
                    elif choice == 3:
                        print(heuristic(nfnode, problem))
                        frontier.push((nfnode, cpath, cprio), cprio + heuristic(nfnode, problem))
                    else:
                        frontier.push((nfnode, cpath))
    "if there are no candidates for expansion then return failure"
    print("Failure! Search could not find a goal!")
    return[]
        
    
    

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
    
    # call chooseSearch to perform DFS, return the path
    return(chooseSearch(0, problem, None))
    

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    # call chooseSearch to perform BFS, return the path
    return(chooseSearch(1, problem, None))

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    
    # call chooseSearch to perform UCS, return the path
    return(chooseSearch(2, problem, None))

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    
    # call chooseSearch to perform A*, return the path
    return(chooseSearch(3, problem, heuristic))
    


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
