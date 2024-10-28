# 테스트 케이스 개수
T = int(input())
for tc in range(1,T+1):
    # 테스트 케이스
    N = int(input())

    # N*N
    arr = [[0]*N for _ in range(N)]
    # if j == 0 -> arr[i][j] = 1
    # if i == j -> arr[i][j] = 1
    # arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
    
    for i in range(N):
    	# 열의 크기는 행의 인덱스+1
        for j in range(i+1):
            if i == j or j == 0:
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
                
    print(f'#{tc}')
    # 0은 출력 안함
    for row in arr:
        result = []
        for x in row:
            if x:
                result += [x]
        print(*result)