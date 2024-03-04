n = int(input())

scared_list = list(map(int,input().split())) #공포도가 큰 애들끼리 먼저 묶어야함

scared_list.sort()
result = 0
count = 0

for i in  scared_list:
    count += 1 #현재 그룹에 해당 모험가를 포함시키기
    if count >= i:
        result += 1
        count = 0
print(result)
        
    
    
    

