t = int(input())
for tc in range(1, t + 1):
    result = 1
    puzzle = [list(map(int, input().split())) for _ in range(9)]
    
    # 행과 열 체크
    for i in range(9):
        row = [0] * 10
        col = [0] * 10
        for j in range(9):
            row[puzzle[i][j]] += 1
            col[puzzle[j][i]] += 1
        for k in range(1, 10):
            if row[k] != 1:
                result = 0
                break
            if col[k] != 1:
                result = 0
                break
        if result == 0:
            break

    # 3x3 구역 체크
    if result == 1:
        for i in range(3):
            for j in range(3):
                rowx = [0] * 10
                for a in range(3):
                    for b in range(3):
                        rowx[puzzle[a + 3 * i][b + 3 * j]] += 1
                for q in range(1, 10):
                    if rowx[q] != 1:
                        result = 0
                        break
                if result == 0:
                    break
            if result == 0:
                break

    print(f"#{tc} {result}")
