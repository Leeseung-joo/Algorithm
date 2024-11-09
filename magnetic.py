t = 10
for tc in range(1,t+1):
    n = int(input())
    list1 = [list(map(int,input().split())) for _ in range(n)]
    total_res = 0
    for i in range(n):
        flag = 0
        for j in range(n):
            if list1[j][i] == 1:
                flag = 1
            elif list1[j][i] == 2:
                if flag:
                    total_res += 1
                    flag = 0
    print(f"#{tc} {total_res}")
