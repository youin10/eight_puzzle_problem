class State :
    def __init__(self, state):
        self.state = state
        self.x = 0
        self.y = 0
        self.size = len(state)
        self.findBlank(state)

    def findBlank(self, state) :

        #0의 위치를 찾는 코드

        pass

    def isActionValid(self, action) :
        isValid = True

        #들어온 action이 유효한지 검사하는 코드
        
        return isValid
