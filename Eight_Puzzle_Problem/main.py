from eight_puzzle import EightPuzzle, Operation, State
from search import breadth_first_tree_search, Node, Problem, depth_limited_search, iterative_deepening_search, astar_search
import time
import random

default_problem = [[1,2,3],[0,4,6],[7,5,8]]
goal = [[1,2,3], [4,5,6], [7,8,0]]
goal2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]

def main () :
    global default_problem
    global goal
    global goal2

    puzzle = EightPuzzle(default_problem, goal)

    startTime = time.time()

    result = depth_limited_search(puzzle, 30)

    #result = breadth_first_tree_search(puzzle)

    endTime = time.time()

    print('solution is ' , Node.solution(result))
    print('path is', Node.path(result))

    print('걸린 시간 :', endTime - startTime)

def mix (initialState, count) :
    state = copy.deepcopy(initialState)

    #퍼즐을 섞는 코드
    
    return state

if __name__ == "__main__" :
    main()
