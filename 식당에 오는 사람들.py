n = int(input())
list1 = []

for _ in range(n):
	arr,lea = map(int,input().split())#arr,lea 각각 도착한 시간,떠난 시간
	list1.append((arr,1))
	list1.append((lea,-1)) #1,-1 각각 도착함, 떠남을 표시 ex)(3,1) --> 3시에 한명 도착
list1.sort() #병합정렬알고리즘임, x축을 기준으로 정렬이 됨.
#풀어야하는 문제: 1명이상 식당에 사람이 존재했던 총 시간s와 사람이 가장 많았을때의 수는?
present_num = 0
max_num = 0
prev_time = -1
total_time = 0


for time,j in list1:
	if j == -1:
		if present_num >= 1:#정렬이 2번째 축에 대해서 작은 값먼저 수행되기 때문에 (7,-1),(7,1)인경우를 고려해서
			total_time += time-prev_time
		present_num += j
	
	else:
		if prev_time > -1 and present_num > 0:
			total_time += time-prev_time
		present_num += j
		max_num = max(present_num,max_num)
	prev_time = time
print(total_time,max_num)