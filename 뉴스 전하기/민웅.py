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