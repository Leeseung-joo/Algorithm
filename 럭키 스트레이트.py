n = input()

k = len(n)
a = sum(int(x) for x in n[:k//2])
b = sum(int(x) for x in n[k//2:]) #/연산자 사용시 부동소수점 반환
if a == b:
    print("LUCKY")
else:
    print("READY")
