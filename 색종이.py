n = int(input())
map_array = [[0]*100 for _ in range(100)] # 100x100 도화지 만들기

for _ in range(n):
    x, y = map(int, input().split())
    # x : x ~ x+10
    # y : y ~ y+10
    for i in range(y, y+10):
        idx_y = i
        # i,j에 해당하는 좌표에 점을 찍음
        for j in range(x, x+10):
            idx_x = j
            if map_array[idx_y][idx_x] == 0:
                map_array[idx_y][idx_x] = 1
            else:
                pass
            
sum_array = 0
for i in range(100):
    sum_array += sum(map_array[i])
print(sum_array)
