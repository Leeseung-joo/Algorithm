t = int(input())
for tc in range(1,t+1):
    n = int(input())
    numbers  = list(map(int,input().split()))
#완전탐색으로 풀어야함
    def dfs(a,b):
        global result
        list1 = []
        str1 = str(numbers[a]*numbers[b])
        for i in range(len(str1)):
            for j in range(i+1,len(str1)):
                     if int(str1[j]) <int(str1[i]):
                         return
        result.append(numbers[a]*numbers[b])
    
    result = []
    for i in range(0,n-1):
        for j in range(i+1,n):
            dfs(i,j)
    if len(result) == 0:
        max_result = -1
    else:
        max_result = max(result)
    print(f"#{tc} {max_result}")
                    
                
        