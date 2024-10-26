T = int(input())

for test_case in range(1, T + 1):
    a = list(input())
    s = 0
    answer = 0
    
    for j in range(1, 10):
        if a[0] != a[j] or a[1] != a[j +1]:
            s += 1
        else:
            break

    answer = s + 1
    print("#%d" %test_case, answer)