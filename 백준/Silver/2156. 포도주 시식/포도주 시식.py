n = int(input())
array = [0]*10000
for i in range(n):
    array[i] = int(input())
    
dp = [0] * 10000
dp[0] = array[0]
dp[1] = array[1]+ dp[0]
dp[2] = max(array[2]+array[0], array[2]+array[1], dp[1])
for i in range(3,n):
        dp[i] = max(dp[i-1], dp[i-3]+ array[i-1]+array[i], dp[i-2]+array[i])
print(dp[n-1])