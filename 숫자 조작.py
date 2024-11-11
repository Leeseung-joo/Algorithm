t = int(input())
for tc in range(1,t+1):
    n = input()
    min_result = 99999999
    max_result = 0
    def dfs(a,b,n_str):
        n_str[a], n_str[b] = n_str[b],  n_str[a]
        return ''.join(n_str)
        
        
    
    
    
    
    
    result = []
    n_str = list(str(n))
    result.append(int(n))
    for i in range(len(n)):
        for j in range(i+1,len(n)):
            value  = dfs(i,j,n_str)
            n_str[i],n_str[j] = n_str[j],n_str[i]
            if value[0] == "0":
                continue
            else:
                result.append(int(value))
        max_result = max(result)
        min_result = min(result)
    print(f"#{tc} {min_result} {max_result}")