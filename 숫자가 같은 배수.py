from itertools import permutations
t = int(input())
for tc in range(1,t+1):
    n = int(input())
    digits = list(str(n))
    flag = "impossible"
    for perm in permutations(digits):
        num = int(''.join(perm))
        if num % n == 0 and len(perm) != 1 and num!=n:
            flag = "possible"
            break
    print(f"#{tc} {flag}")