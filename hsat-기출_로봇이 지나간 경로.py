h,w = map(int,input().split())
matrix = [list(input() for _ in range(h))]

directionMark = ["^", "<", "v", ">"]

dx = [-1,0,1,0] #dx,dy 방향 외우기
dy = [0,-1,0,1]
def findDirection(x,y):
    count = 0
    for i in range(4):
        nx,ny = x+dx[i], y+dy[i]
        if 0<=nx <h and 0<=ny <w and matrix[nx][ny] == "#":
             direction = i
             count += 1
    return (direction if count == 1 else -1)

def findStart(matrix):
    for x in range(h):
        for y in range(w):
            if matrix[x][y] == "#":
                direction = findDirection(x,y) #현재 위치에서 좌우 상하를 보고 어디에 #이 있는지를 알려주는 함수
                if direction != -1:            # 하나만 있는 경우가 아니면 다 -1을 리턴하도록 설계
                    return x,y,direction
def navigate(x,y,direction):
    newDir = preDir = direction
    matrix[x][y] = '.'
    while True:
        while newDir == preDir:
            print('A', end = '')
            x,y = x+dx[newDir], y+dy[newDir]
            matrix[x][y] = '.'
            x,y = x+dx[newDir], y+dy[newDir]
            matrix[x][y] = '.'
            
            preDir = newDir
            newDir = findDirection(x,y)
        if newDir == -1:
            return
        elif (newDir - preDir) % 4 == 1:
            print("L", end = '')
        elif (newDir-preDir) % 4 == 3:
            print ('R', end = '')
        preDir = newDir
            




x,y,direction = findStart(matrix) #스타트할 끝점
print(x+1,y+1)
print(directionMark(direction))
navigate(x,y,direction)