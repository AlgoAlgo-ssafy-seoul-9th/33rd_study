# 1189_컴백홈_comebackhome
# 92ms
import sys
input = sys.stdin.readline
dxy = [(1, 0), (-1, 0), (0, -1), (0, 1)]

def bt(x, y, v, score):
    global ans
    if x == 0 and y == C-1:
        if score == K:
            ans += 1
        return

    if score >= K:
        return

    for d in dxy:
        nx = x + d[0]
        ny = y + d[1]
        if 0 <= nx <= R-1 and 0 <= ny <= C-1:
            if not v[nx][ny] and field[nx][ny] != 'T':
                v[nx][ny] = 1
                bt(nx, ny, v, score + 1)
                v[nx][ny] = 0


R, C, K = map(int, input().split())

field = [list(input().strip()) for _ in range(R)]

i, j = R-1, 0
ans = 0
visited = [[0]*C for _ in range(R)]
visited[i][j] = 1
bt(i, j, visited, 1)

print(ans)