from collections import deque
t = int(input())
for i in range(t): # for else문: break등으로 중간에 빠져나오지 않고 끝까지 실행됬을 경우 else문이 실행
    a = input()
    d = deque()
    for j in a:
        if j == "(":
            d.append(j)
        elif j == ")":
            if d:
                d.pop()
            else:
                print("NO")
                break
    else:
        if not d:
            print("YES")
        else:
            print("NO")