n = int(input())
list1 = list(map(int,input))
dp = [0] * n
dp[0] = list1[0]
for i in range(1,n):
    dp[i] = max(list1[i], list1[i]+dp[i-1]) #현재꺼 혹은 이전 최대 연속합 + 현재
print(max(dp))