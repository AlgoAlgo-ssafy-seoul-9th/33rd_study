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

