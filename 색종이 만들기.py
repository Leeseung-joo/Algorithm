import sys
input = sys.stdin.readline
n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
white = 0
blue = 0

def solution(x, y, n):
    global white, blue  # global 키워드 추가
    color = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != paper[i][j]:
                solution(x, y, n // 2)
                solution(x, y + n // 2, n // 2)
                solution(x + n // 2, y, n // 2)
                solution(x + n // 2, y + n // 2, n // 2)
                return
    if color == 0:  # 하나의 색깔로 통일된 경우
        white += 1
    else:
        blue += 1

solution(0, 0, n)
print(white)
print(blue)
