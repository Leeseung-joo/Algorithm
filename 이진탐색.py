n = int(input())
list1 = list(map(int, input().split()))
k = int(input())

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
		elif left == len(list1):
			return A[-1]
		else:
			if item - A[left-1] < A[left] - item:
				return A[left-1]
			else:
				return A[left]
			
			
			
		
p = binarysearch(list1,k,0, n-1)
print(p)
