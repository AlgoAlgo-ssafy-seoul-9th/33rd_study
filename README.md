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
