array = [1,3,4,2,5,6,7,9,8]

for i in range(len(array)):
    min_index = i
    for j in range(i+1,len(array)):
        if array[min_index] > j:
            min_index = j
    array[min_index], array[i] = array[i],array[min_index]

print(array)