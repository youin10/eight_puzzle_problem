# eight_puzzle_problem

타일을 움직여 제자리로 맞추는 Eight puzzle 문제입니다.

문제의 state 표현은 다음과 같습니다.

[[1,2,3], [4,5,6], [7,8,0]]

이중 리스트로 표현이 되며 0은 빈칸을 의미합니다. 위의 상태는 실제 퍼즐의 형태로 다음과 같습니다.

 1 | 2 | 3 
 
 4 | 5 | 6 
 
 7 | 8 |    
 
 문제의 action은 다음의 4개입니다.
 
 up, down, left, right
 
 각 action은 단어의 의미에 따라 빈칸을 움직이는 것입니다.
 
 search 알고리즘을 통해 문제를 해결하기 위해선 State 클래스와 Operation 클래스를 완성하여야 합니다.
 
 State 클래스는 위에서 정의한 state를 받아 빈 칸의 위치를 찾는 findBlank 함수와 주어진 action이 현재 state에 적용 가능한지의 여부를 판단하는 isValidAction 함수를 작성하여야 합니다.
 
 Operation 클래스는 주어진 state에 주어진 action을 수행하여 얻어지는 결과 state를 반환하는 moveBlank 함수를 작성하여야 합니다.
 
 코드 테스트는 main.py 파일을 실행하면 됩니다.
