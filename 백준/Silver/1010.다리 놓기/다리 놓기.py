import sys
import math
input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())
    print(math.comb(M,N))

if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        solve()