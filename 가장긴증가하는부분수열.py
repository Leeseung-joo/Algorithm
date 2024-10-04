# n = int(input()) 처음 잘못 푼 풀이
# array = list(map(int,input().split()))
# result = 1
# for j in range(n):
#     prev = array[j]
#     length = 1
#     for i in range(j,n-1):
#         if array[i+1]>prev:
#             length += 1
#             prev = array[i+1]
#     result = max(result,length)
# print(result)
       
n = int(input())
array = list(map(int, input().split()))
#dp[i]는 i번쨰 원소를 마지막 원소로 하는 LIS의 길이
dp = [1]*n 
for i in range(1,n):
    for j in range(i):
        if array[i] > array[j]:
            dp[i] = max(dp[i], dp[j]+1) #증가하는 경우
            
result = max(dp)
print(result)