
n,m = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 2:
            a,b = i,j
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            matrix[i][j] = abs(i-a+j-b)
        elif matrix[i][j] == 2:
            matrix[i][j] = 0
        else:
            continue
for i in range(m):
    for j in range(n):
        print(matrix[i][j], end = ' ')
    print(sep = '\n')
