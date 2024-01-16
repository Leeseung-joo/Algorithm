array = [1,3,4,2,5,6,7,9,8]

for i in range(1,len(array)):
    for j in range(i,0,-1):
        if array[j] < array[j-1]:
            array[j],array[j-1] = array[j-1],array[j]
        else: #자기보다 작은 데이터를 만나면 멈춤
            break
print(array)