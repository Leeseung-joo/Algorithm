t = int(input())
for tc in range(1,t+1):
    n = int(input())
    list1 = [list(map(int,input().split())) for _ in range(n)]
    list1_90 = [[0]*n for _ in range(n)]
    list1_180 = [[0]*n for _ in range(n)]
    list1_270 = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            list1_90[i][j] = list1[n-1-j][i]
            list1_180[i][j] = list1[n-1-i][n-1-j]
            list1_270[i][j] = list1[j][n-1-i]
    str1,str2,str3 = "", "", ""
    for a in range(n):
        for b in range(n):
            str1 = str1+str(list1_90[a][b])
            str2  = str2 + str(list1_180[a][b])
            str3 = str3 + str(list1_270[a][b])
    print(f"#{tc}")
    for i in range(1,n+1):
        print(f"{str1[n*(i-1):n*i]} {str2[n*(i-1):n*i]} {str3[n*(i-1):n*i]}")