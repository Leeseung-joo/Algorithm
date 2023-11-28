n = int(input())  # 위쪽 교차로의 개수
ud = list(map(int, input().split()))  # u에서 한 칸 가는 것
ul = list(map(int, input().split()))  # u에서 l로 가는 것
ld = list(map(int, input().split()))  # l에서 한 칸 가는 것
lu = list(map(int, input().split()))  # l에서 u로 가는 것
un = [0] * (n + 1)
ln = [0] * (n + 1)
for i in range(1, n + 1):
    if i == 1:
        un[i - 1] = min(ud[i - 1], ld[i - 1] + lu[i - 1])
        ln[i - 1] = min(ld[i - 1], ud[i - 1] + ul[i - 1])
        # print(un[i-1])
        # print(ln[i-1])
    else:
        un[i - 1] = min((un[i - 2] + ud[i - 1]), (ln[i - 2] + ld[i - 1] + lu[i - 1]))
        ln[i - 1] = min((ln[i - 2] + ld[i - 1]), (un[i - 2] + ud[i - 1] + ul[i - 1]))
        # print(un[i-1],i-1)
        # print(ln[i-1])

min_result = min((un[n-1] + ud[-1]),(ln[n-1]+ld[-1]))


print(min_result)
