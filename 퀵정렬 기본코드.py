array = [0,2,4,1,5,6,7,8,3]

def quic_sort(array,start,end):
    if start >= end:   #원소가 1개이면 종료
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right: #left가 right보다 더 커져버리면 작은데이터인 right과 피봇값을 교체후 while문 종료
        while left <= end and array[left] <= array[pivot]: #피봇보다 큰 값을 찾아야함
            left += 1
        while right > start and array[right] >= array[pivot]: #여기서 등호가 빠진 이유는 등호가 들어가면 right가 start랑 같고 pivot값보다 값이 커져버리면 right가 피봇위치랑 같아져버리기때문이다.
            right -= 1
        if left > right:
            array[right], array[pivot] = array[pivot],array[right] #엇갈리면 작은값과 교체
        else:
            array[left],array[right] = array[right],array[left]
    quic_sort(array,start,right-1)
    quic_sort(array,right+1,end)

quic_sort(array,0,len(array)-1)
print(array)
