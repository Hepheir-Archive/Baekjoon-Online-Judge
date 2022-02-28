import sys
import collections
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def get_max_construction_delay(target:int, delay:list, required:{list}):
    memoization_max_construction_delay = collections.defaultdict(int)
    def _max_construction_delay(target):
        nonlocal delay, required
        if target in memoization_max_construction_delay:
            return memoization_max_construction_delay[target]
        elif target not in required:
            return delay[target]
        memoization_max_construction_delay[target] = delay[target] + max(map(_max_construction_delay, required[target]))
        return memoization_max_construction_delay[target]
    return _max_construction_delay(target)

    
def solve():
    N, K = map(int, input().split())
    D = list(map(int, input().split()))
    required = collections.defaultdict(list)
    for k in range(K):
        X, Y = map(lambda x: int(x)-1, input().split())
        required[Y].append(X)
    W = int(input())-1
    return get_max_construction_delay(W, D, required)

if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        print(solve())