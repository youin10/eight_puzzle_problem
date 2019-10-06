from search import Problem
from .state import State
from .operation import Operation

class EightPuzzle(Problem) :
    def __init__(self, initial, goal = None):
        self.initial = initial
        self.goal = goal 

    def getAllActions(self) : 
        return [
            'up',
            'down',
            'left',
            'right'
        ]

    def actions(self, state) :
        return self.getValidAction(state, self.getAllActions()) 

    def result(self, state, action) :
        operator = Operation()
        next = operator.moveBlank(state, action)
        return next

    def getValidAction(self, state, allActions) :
        validActionSet = set() 
        s = State(state) 

        for action in allActions :
            if s.isActionValid(action) :
                validActionSet.add(action)
            else :
                pass
        
        return validActionSet
    
    def goal_test(self, state) :
        return state == self.goal