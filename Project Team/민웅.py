# 20044_Project Teams
import sys
input = sys.stdin.readline

N = int(input())

n_lst = list(map(int, input().split()))
n_lst.sort()

ans = float('inf')
for i in range(N):
    tmp = n_lst[i] + n_lst[-1-i]
    if tmp < ans:
        ans = tmp

print(ans)