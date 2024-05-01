import sys
input = sys.stdin.readline

def sol(x, y, dis, visited):
    # print(x, y, dis, visited)
    if x == 0 and y == C-1:
        if dis == K:
            ans += 1
            return
        else:
            return
    if 0 <= x-1 < R and not visited[x-1][y] and  arr[x-1][y] != 'T': 
        visited[x-1][y] = 1
        sol(x-1, y, dis+1, visited)
    elif 0 <= y+1 < C and not visited[x][y+1] and arr[x][y+1] != 'T':
        visited[x][y+1] = 1
        sol(x, y+1, dis+1, visited)
    elif 0 <= x+1 < R and not visited[x+1][y] and arr[x+1][y] != 'T':
        visited[x+1][y] = 1
        sol(x+1, y, dis+1, visited)
    elif 0 <= y-1 < C and not visited[x][y-1] and arr[x][y-1] != 'T':
        visited[x][y-1] = 1
        sol(x, y-1, dis+1, visited)
    else:
        return

R, C, K = map(int, input().split())
arr = [list(map(str, input().strip())) for _ in range(R)]
ans = 0
visited = [[0]*C for _ in range(R)]
sol(R-1, 0, 0, visited)

print(ans)