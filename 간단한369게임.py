n = int(input())
array = []
for i in range(1,n+1):
    cnt = str(i).count('3')+str(i).count('6')+str(i).count('9')
        
    if cnt == 0:
        array.append(i)
    else:
        array.append('-'*cnt)
for j in array:
    print(j, end = ' ')
        
    