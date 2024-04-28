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
