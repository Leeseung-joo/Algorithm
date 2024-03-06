n = int(input())

scared_list = list(map(int,input().split())) #공포도가 큰 애들끼리 먼저 묶어야함

scared_list.sort()
result = 0
count = 0

for i in  scared_list:
    count += 1 #현재 그룹에 해당 모험가를 포함시키기
    if count >= i: #현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        result += 1 #총 그룹의 수 증가
        count = 0 #현재 그룹에 포함된 모험가의 수 초기화
print(result)
        
    
    
    

