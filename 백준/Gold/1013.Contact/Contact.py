import sys
input = sys.stdin.readline

STATE_MACHINE = {
    0: (1,2),
    1: (-1,0),
    2: (3,-1),
    3: (4,-1),
    4: (4,5),
    5: (1,6),
    6: (7,6),
    7: (4,0)}

def solve():
    data = input().rstrip()
    state = 0
    for d in map(int, data):
        state = STATE_MACHINE[state][d]
        if state == -1:
            break
    if state in (0,5,6):
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        print(solve())