m = int(input())
alist = list(map(int,input().split()))
n = int(input())
blist = list(map(int,input().split()))

def binarysearch(A, item, left, right):
	if left <= right:
		mid = (left+right)//2
		if item == A[mid]:
			return item
		elif item < A[mid]:
			return binarysearch(A, item, left, mid-1)
		else:
			return binarysearch(A,item,mid+1,right)
	else:
		if right == -1:
			return A[0]
		elif left == len(alist):
			return A[-1]
		else:
			if item - A[left-1] < A[left] - item:
				return A[left-1]
			else:
				return A[left]

difference_min = 100
pair = (0, 0)
for i in blist:
	number = binarysearch(alist, i, 0, m-1) #alist에서의 값임 이건
	difference= abs(number - i) #i는 blist에서의 값
	if difference < difference_min or (difference == difference_min and number > pair[0]) or (difference == difference_min and number == pair[0] and i > pair[1]) :
		difference_min = difference
		pair = (number,i)

print(difference_min)

print(pair[0],pair[1])