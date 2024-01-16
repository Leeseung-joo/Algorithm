def binary_search(array,target,start,end):
    while start <= end:
        mid = (start+end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid -1
        else:
            start = mid+1
    return None #반복문안에서 return을 하지못하고 나왔으면 해당하는 값이 없는 것이므로 None반환

n,target = list(map(int,input().split()))
array = list(map(int,input().split()))

result = binary_search(array,target,0,n-1)
if result == None:
    print("원소가 존재하지 않습니다")
else:
    print(result)