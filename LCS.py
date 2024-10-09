import sys
input = sys.stdin.readline
string_a = input().strip()
string_b = input().strip()
dp = [0]*1000
for i in range(string_a):
    for j in range(string_b):
        if string_a[i] == string_b[j]:
            