t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    list1 = [[0] * n for _ in range(n)]
    dx = [0, 1, 0, -1]  # 오른쪽, 아래, 왼쪽, 위쪽 순서
    dy = [1, 0, -1, 0]

    def snail(x, y, d, num):
        list1[x][y] = num
        if num == n * n:
            return
        nx = x + dx[d]
        ny = y + dy[d]
        if nx < 0 or ny < 0 or nx >= n or ny >= n or list1[nx][ny] != 0:
            d = (d + 1) % 4
            nx = x + dx[d]
            ny = y + dy[d]
        snail(nx, ny, d, num + 1)

    # 각 테스트 케이스마다 snail 함수 호출
    snail(0, 0, 0, 1)
    
    # 출력
    print(f"#{tc}")
    for i in range(n):
        print(" ".join(map(str, list1[i])))
