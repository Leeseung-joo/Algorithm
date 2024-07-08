n = int(input())
listn = list(map(int,input().split()))
listn.sort()
m = int(input())
listm = list(map(int,input().split()))

    
def binary_search(array,target,start,end):
    if start > end:
        return None
    mid = (start+end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] < target:
        return binary_search(array,target,mid+1,end)
    else:
        return binary_search(array,target,start,mid-1)
    
    




for i in listm:
    k = binary_search(listn,i,0,n-1)
    if k == None:
        print("0")
    else:
        print("1")