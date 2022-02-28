import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def bfs(land, gn, x, y):
    if 0 <= x < width and 0 <= y < height:
        if land[y][x] == 0:
            land[y][x] = gn
            bfs(land, gn, x-1, y)
            bfs(land, gn, x+1, y)
            bfs(land, gn, x, y-1)
            bfs(land, gn, x, y+1)

def solve():
    global width, height, land
    width, height, n_cabbages = map(int, input().split())
    land = [[-1] * width for y in range(height)]
    for k in range(n_cabbages):
        x, y = map(int, input().split())
        land[y][x] = 0
    n_groups = 0
    for x in range(width):
        for y in range(height):
            if land[y][x] == 0:
                n_groups += 1
                bfs(land, n_groups, x, y)
    return n_groups


if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        print(solve())