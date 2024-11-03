t = int(input())
for tc in range(t):
    n = int(input())
    list1 = list(map(int, input().split()))
    frequency_dict = {}
    max_cnt = 0
    max_value = 0
    
    while len(list1) != 0:
        value = list1.pop()
        if value in frequency_dict:
            frequency_dict[value] += 1
        else:
            frequency_dict[value] = 1

    for value, cnt in frequency_dict.items():
        if cnt > max_cnt:
            max_cnt = cnt
            max_value = value  # 최빈값 갱신
        elif cnt == max_cnt:
            if value > max_value:
                max_value = value  # 큰 값으로 갱신
    
    print(f"#{tc + 1} {max_value}")
