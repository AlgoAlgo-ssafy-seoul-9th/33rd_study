import sys
input = sys.stdin.readline

n = int(input())
w = list(map(int, input().split()))

w.sort()
minW = 200000
for i in range(n):
    can = w[i]+w[n*2-1-i]
    minW = min(can, minW)
print(minW)