for tc in range(1,11):
    T = int(input())
    arr = [input() for _ in range(100)]
    max_result = 0
    length = 0
    for i in range(100): # 행 번호
        for j in range(100, length, -1): # 회문 길이
            result = 0
            for k in range(101 - j): # 열번호
                if result:
                    break
                for m in range(j):
                    if arr[i][k+m] == arr[i][k+j-m-1]:
                        result += 1
                    else:
                        result = 0
                        break
                if max_result < result:
                    max_result = result
                    length = result
    for i in range(100):
        for j in range(100,length,-1):
            result  = 0
            for k in range(101-j):
                if result:
                    break
                for m in range(j):
                    if arr[k+m][i] == arr[k+j-m-1][i]:
                        result += 1
                    else:
                        result = 0
                        break  
                if max_result <result:
                    max_result = result
                    length = result  
    print(f"#{T} {max_result}")