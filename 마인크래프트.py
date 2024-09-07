import sys
input = sys.stdin.readline

n,m,b = map(int,input().split())
block = [] #m은 0부터 256까지
for _ in range(n):
    block.append(list(map(int,input().strip().split())))
    
ans = int(1e9)
glevel = 0

for i in range(257):
    use_block = 0
    take_block = 0
    for x in range(n):
        for y in range(m):
            if block[x][y] > i:
                take_block += block[x][y] - i
            else:
                use_block += i - block[x][y]
                
    if use_block > take_block + b:
        continue
    
    count = take_block *2 + use_block
    
    if count <= ans:
        ans = count
        glevel = i
print(ans, glevel)