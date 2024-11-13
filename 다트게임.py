import math
 
T = int(input()) # 테스트 케이스의 수 T
ans = []
 
for test_case in range(1, T+1):
 
    N = int(input()) # 화살의 개수 N
    answer = 0
 
    for _ in range(N):
        x, y = map(int, input().split()) # 화살이 떨어진 위치 x, y
        score = math.ceil(math.sqrt(x*x+y*y)/20) # 위치에 따른 점수 계산
 
        if(score==0):
            answer += 10
        elif score <= 10:
            answer += 11-score
    ans.append(f'#{test_case} {answer}')
for a in ans:
    print(a)
