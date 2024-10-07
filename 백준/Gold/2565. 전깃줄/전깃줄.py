n = int(input())
list1 = []
dp = [1]*n

for i in range(n):
    a,b = map(int,input().split())
    list1.append([a, b])

list1.sort()

for i in range(1,n):
    for j in range(0,i):
        if list1[j][1] < list1[i][1]:
            dp[i] = max(dp[i], dp[j]+1)
print(n-max(dp))