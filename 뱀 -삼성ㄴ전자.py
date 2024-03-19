n = int(input())
k = int(input())
data = [[0] *(n+1) for _ in range(n+1)] #맵 정보, 헷갈리지않게하기위해 n+1로 하기
info = [] #방향회전정보

#맵 정보(사과 있는 곳은 1로 표시)
for _ in range(k):
    a,b = map(int,input().split())
    data[a][b] = 1    
    
#방향회전 정보 입력
l = int(input())
for _ in range(l):
    x,c = input().split()
    info.append((int(x),c))
    
dx = [0,1,0,-1] #동남서북
dy = [1,0,-1,0]

def simulate():
    x,y = 1,1
    data[x][y] = 2 #뱀이 존재하는 위치는 2로 표시
    direction = 0 #처음에 동쪽을 바라보고 있음
    time = 0
    q = [(x,y)] #뱀이 차지하고 있는 위치정보
    index = 0 #다음에 회전할 정보
def turn(direction, c):
    if c == "L":
        direction = (direction-1) % 4
    else:
        direction = (direction + 1) % 4
    return direction
    
    
    
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and data[nx][ny] != 2:
            if data[nx][ny] == 0: #사과가 없다면 이동 후에 꼬리 제거
                data[nx][ny] = 2
                q.append((nx,ny))
                px,py = q.pop(0)
                data[px][py] = 0
            if data[nx][ny] == 1:
                data[nx][ny] = 2
                q.append((nx,ny))
        else:
            time += 1
            break
        x,y = nx,ny #다음위치로 머리를 이동
        time += 1
        if index < l and time == info[index][0]:
            direction = turn(direction, info[index][1])
            index += 1
    return time
    
    
    