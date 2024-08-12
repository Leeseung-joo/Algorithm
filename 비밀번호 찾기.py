import sys
input = sys.stdin.readline
n,m = map(int,input().strip().split())
program = {}
for i in range(n):
    site,password = map(str,input().strip().split())
    program[site] = password
    
for _ in range(m):
    site = input().strip()
    print(program[site])