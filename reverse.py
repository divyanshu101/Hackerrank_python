import sys


n = int(input().strip())
arr = list(map(int,input().strip().split(' ')))
ans = ""

print(*arr[::-1])