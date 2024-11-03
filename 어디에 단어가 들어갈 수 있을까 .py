t = int(input())

for tc in range(1, t + 1):
    n, k = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(n)]
    result = 0

    # 행(row) 방향으로 K 길이의 단어가 들어갈 수 있는 자리 수 계산
    for i in range(n):
        cnt = 0
        for j in range(n):
            if puzzle[i][j] == 1:  # 빈칸(1)인 경우
                cnt += 1
            else:  # 벽(0)을 만나면
                if cnt == k:  # K 길이의 연속된 빈칸을 찾았을 때
                    result += 1
                cnt = 0  # cnt 초기화
        if cnt == k:  # 행 끝에서 K 길이의 연속된 빈칸이 있을 때
            result += 1

    # 열(column) 방향으로 K 길이의 단어가 들어갈 수 있는 자리 수 계산
    for j in range(n):
        cnt = 0
        for i in range(n):
            if puzzle[i][j] == 1:  # 빈칸(1)인 경우
                cnt += 1
            else:  # 벽(0)을 만나면
                if cnt == k:  # K 길이의 연속된 빈칸을 찾았을 때
                    result += 1
                cnt = 0  # cnt 초기화
        if cnt == k:  # 열 끝에서 K 길이의 연속된 빈칸이 있을 때
            result += 1

    print(f"#{tc} {result}")
