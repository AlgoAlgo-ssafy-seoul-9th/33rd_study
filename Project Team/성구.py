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

