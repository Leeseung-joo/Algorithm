n = int(input())
k = 1
for i in range(n,1, -1):
    k *= i
str1 = str(k)
cnt = 0
for j in str1[-1::-1]:
    if j == '0':
        cnt += 1
    else:
        break
    
print(cnt)
