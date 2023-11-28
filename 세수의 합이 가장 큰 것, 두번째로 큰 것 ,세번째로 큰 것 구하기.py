n = int(input())
list1 = list(map(int, input().split()))
import random

def quicksort(A,left,right):
	if left<right:
		pivotpoint = partition(A,left,right)
		quicksort(A,left,pivotpoint-1)
		quicksort(A,pivotpoint+1,right)
def partition(A,left,right):
	random_index = random.randint(left,right)
	A[random_index],A[right] = A[right],A[random_index]
	pivot = A[right]
	pivotpoint = left-1
	for i in range(left,right):
		if (A[i] <= pivot):
			pivotpoint += 1
			A[i], A[pivotpoint] = A[pivotpoint], A[i]
	pivotpoint += 1
	A[pivotpoint], A[right] = A[right],A[pivotpoint]
	return pivotpoint
	
if sorted(list1) != list1:
	quicksort(list1,0,n-1)
else:
	max1= list1[-1]+list1[-2]+list1[-3]
	max2= list1[-1]+list1[-2]+list1[-4]
	max3= list1[-1]+list1[-2]+list1[-5]
	print(max1,max2,max3)
	exit()
max1= list1[-1]+list1[-2]+list1[-3]

i = 4
while True:
	if list1[-3] == list1[-i]:
		i+=1
	else:
		break
k = i          #list1[-(i+k+m+1)]이 4번째로 큰 값이다. 그러면 max3 = list1[-1]+list1[-(i+k+1)] + list1[-                (i+k+m+1)]이랑 비교
i+=1
while True:
	if list1[-k] == list1[-i]:
		i+=1
	else:   
		break
a = list1.count(list1[-1])  #1번째로 큰 수
b = list1.count(list1[-(a+1)]) #2번째로 큰 수
c = list1.count(list1[-(a+b+1)]) #3번째 로 큰 수

max2 = list1[-1]+list1[-2]+list1[-k]
max3 = max((list1[-1]+list1[-2]+list1[-i]), list1[-1]+list1[-(a+b+1)]+list1[-(a+b+c+1)] )   # 두 경우 중 큰거를 max3로 취함. 
print(max1,max2,max3)	


