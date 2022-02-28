import sys
input = sys.stdin.readline

CHEAT = {
    0: [0],
    1: [1],
    2: [2,4,8,6],
    3: [3,9,7,1],
    4: [4,6],
    5: [5],
    6: [6],
    7: [7,9,3,1],
    8: [8,4,2,6],
    9: [9,1]
}

def solve():
    A, B = map(int, input().split())
    a = A % 10
    b = B % len(CHEAT[a])
    ans = CHEAT[a][b-1]
    return ans if ans else 10

if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        ans = solve()
        print(ans)