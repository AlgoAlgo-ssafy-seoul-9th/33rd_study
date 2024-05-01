# 33rd_study

알고리즘 스터디 33주차

<br/>

# 이번주 스터디 문제

<details markdown="1" open>
<summary>접기/펼치기</summary>

<br/>

## [컴백홈](https://www.acmicpc.net/problem/1189)

### [민웅](./컴백홈/민웅.py)

```py
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
```

### [상미](./컴백홈/상미.py)

```py
import sys
input = sys.stdin.readline

def sol(x, y, dis, visited):
    global ans
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
        visited[x-1][y] = 0
    if 0 <= y+1 < C and not visited[x][y+1] and arr[x][y+1] != 'T':
        visited[x][y+1] = 1
        sol(x, y+1, dis+1, visited)
        visited[x][y+1] = 0
    if 0 <= x+1 < R and not visited[x+1][y] and arr[x+1][y] != 'T':
        visited[x+1][y] = 1
        sol(x+1, y, dis+1, visited)
        visited[x+1][y] = 0
    if 0 <= y-1 < C and not visited[x][y-1] and arr[x][y-1] != 'T':
        visited[x][y-1] = 1
        sol(x, y-1, dis+1, visited)
        visited[x][y-1] = 0


R, C, K = map(int, input().split())
arr = [list(map(str, input().strip())) for _ in range(R)]
ans = 0
visited = [[0]*C for _ in range(R)]
visited[R-1][0] = 1
sol(R-1, 0, 1, visited)

print(ans)
```

### [성구](./컴백홈/성구.py)

```py
# 1189 컴백홈
import sys
input = sys.stdin.readline
# bfs 보다 dfs가 빠름 200ms vs 160ms

def main():
    R, C, K = map(int, input().split())
    field = tuple(input().strip() for _ in range(R))

    # dfs
    def dfs():
        # set구조를 이용하여 2차원 배열을 넘버링하여 visited 처리
        stack = [(R-1, 0, set([(R-1)*C]))]
        cnt = 0
        while stack:
            i, j, visited = stack.pop()
            if (i,j) == (0, C-1):
                if len(visited) == K:
                    # print(visited)
                    cnt += 1
                continue

            # 가지치기
            if len(visited) >= K:
                continue

            for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                ni, nj = di + i, dj + j
                if 0 <= ni < R and 0 <= nj < C:
                    if field[ni][nj] != "T" and (ni*C+nj) not in visited:
                        stack.append((ni,nj, visited.union(set([ni*C+nj]))))

        return cnt


    print(dfs())

    return


if __name__ == "__main__":
    main()


```

### [영준](./컴백홈/영준.py)

```py

```

<br/>

## [뉴스 전하기](https://www.acmicpc.net/problem/1135)

### [민웅](./뉴스%20전하기/민웅.py)

```py
# 1135_뉴스 전하기_delivering news
import sys
input = sys.stdin.readline

def tree_traversal(node):
    if not child_node[node]:
        dp[node] = 0
    else:
        child_lst = []
        for c in child_node[node]:
            tree_traversal(c)
            child_lst.append(dp[c]+1)

        child_lst.sort(reverse=True)
        # print(child_lst)
        for i in range(len(child_lst)):
            dp[node] = max(dp[node], child_lst[i]+i)


N = int(input())

root, *tree_info = map(int, input().split())
child_node = [[] for _ in range(N)]
dp = [0]*N
# print(tree_info)

for i in range(N-1):
    child_node[tree_info[i]].append(i+1)

tree_traversal(0)

print(dp[0])
```

### [성구](./뉴스%20전하기/성구.py)

```py
# 1135 뉴스 전하기
import sys
input = sys.stdin.readline


def main():
    # 연락할 사람 수를 비교하면서 트리순회
    N = int(input())
    members = tuple(map(int, input().split()))
    trees = [[] for _ in range(N)]
    # 트리 만들기
    for idx in range(1, N):
        trees[members[idx]].append(idx)
    # 트리 순회
    def tree_circuit(member:int) -> int:
        calls = []      # 연락할 사람 수 리스트
        for c in trees[member]:
            # 재귀 탐색을 통해 가장 큰 경우만 가져옴
            calls.append(1+tree_circuit(c))

        if calls:
            calls.sort(reverse=1)   # 역순 정렬
            # 순번 비용 추가
            for i in range(len(calls)):
                calls[i] += i
            return max(calls)   # 가장 큰 값만 전달
        return 0        # 리스트가 비어있으면 (연락할 사람이 없으면)
    print(tree_circuit(0))
    return


if __name__ == "__main__":
    main()

```

### [상미](./뉴스%20전하기/상미.py)

```py

```

### [영준](./뉴스%20전하기/영준.py)

```py

```

<br/>

## [Project Team](https://www.acmicpc.net/problem/20044)

### [민웅](./Project%20Team/민웅.py)

```py
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
```

### [상미](./Project%20Team/상미.py)

```py
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
```

### [성구](./Project%20Team/성구.py)

```py
# 20044 Project Teams
import sys
input = sys.stdin.readline


def main():
    N = int(input())
    members = sorted(list(map(int, input().split())))

    # 최소와 최대를 더한다
    # 0번째와 2N-1번째 팀, 1번째와 2N-2번째 팀
    for i in range(N):
        members[i] += members[(2*N-1-i)]
    # 그중 최솟값 반환
    print(min(members[:N]))
    return


if __name__ == "__main__":
    main()


```

### [영준](./Project%20Team/영준.py)

```py

```

<br/>

</details>

<br/><br/>

# 지난주 스터디 문제

<details markdown="1">
<summary>접기/펼치기</summary>

<br/>

## [프로세서 연결하기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV4suNtaXFEDFAUf)

### [민웅](./프로세서%20연결하기/민웅.py)

```py
# SWEA_프로세서연결하기
import sys
input = sys.stdin.readline
dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]

T = int(input())


def bt(idx, core_cnt, total_dis, picked_lines):
    global c_cnt, ans
    if idx == len(points):
        if core_cnt > c_cnt:
            ans = total_dis
            c_cnt = core_cnt
        elif core_cnt == c_cnt and total_dis < ans:
            ans = total_dis
        return

    sp = points[idx]

    for ep in lines[idx]:
        now_line = (sp, ep)
        for bl in picked_lines:
            if is_cross(now_line, bl):
                break
        else:
            picked_lines.append(now_line)
            bt(idx+1, core_cnt+1, total_dis + distance(sp, ep), picked_lines)
            picked_lines.pop()

    bt(idx+1, core_cnt, total_dis, picked_lines)


def is_cross(l1, l2):
    s1, e1 = l1
    s2, e2 = l2

    # 선분1이 수평
    if s1[0] == e1[0]:
        # 선분2도 수평
        if s2[0] == e2[0]:
            # 다른라인이면 안겹침
            if s1[0] != s2[0]:
                return False
            if s1[1] > e2[1] or e1[1] < s2[1]:
                return False
        # 선분2는 수직
        else:
            if min(s1[1], e1[1]) <= s2[1] <= max(s1[1], e1[1]) and min(s2[0], e2[0]) <= s1[0] <= max(s2[0], e2[0]):
                return True
            else:
                return False
    else:
        # 선분1 수직, 선분2 수평
        if s2[0] == e2[0]:
            if min(s1[0], e1[0]) <= s2[0] <= max(s1[0], e1[0]) and min(s2[1], e2[1]) <= s1[1] <= max(s2[1], e2[1]):
                return True
            else:
                return False
        # 선분2도 수직
        else:
            if s1[1] != s2[1]:
                return False
            if s1[0] > e2[0] or e1[0] < s2[0]:
                return False

    return True


def distance(s, e):
    return abs(e[0] - s[0]) + abs(e[1] - s[1])


for tc in range(1, T+1):
    N = int(input())
    cores = [list(map(int, input().split())) for _ in range(N)]

    points = []
    side_points = []
    c_cnt = 0
    ans = 0

    for i in range(N):
        for j in range(N):
            if cores[i][j]:
                if i == 0 or i == N-1 or j == 0 or j == N-1:
                    side_points.append((i, j))
                else:
                    points.append((i, j))

    lines = [[] for _ in range(len(points))]

    for i in range(len(points)):
        p = points[i]
        start = (p[0], p[1])
        for d in dxy:
            nx = p[0] + d[0]
            ny = p[1] + d[1]
            end = 0
            while 0 <= nx <= N-1 and 0 <= ny <= N-1:
                if cores[nx][ny] == 1:
                    end = 0
                    break
                end = (nx, ny)
                nx += d[0]
                ny += d[1]

            if end:
                lines[i].append(end)

    bt(0, 0, 0, [])

    # print(lines)
    # print(c_cnt, ans)
    print(f'#{tc} {ans}')
```

### [상미](./프로세서%20연결하기/상미.py)

```py

```

### [성구](./프로세서%20연결하기/성구.py)

```py

```

### [영준](./프로세서%20연결하기/영준.py)

```py

```

</details>

<br/><br/>

# 알고리즘 설명

<details markdown="1">
<summary>접기/펼치기</summary>

</details>
