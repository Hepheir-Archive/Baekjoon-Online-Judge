import sys
input = sys.stdin.readline

def euclidean_dist(src_x,src_y,dst_x,dst_y):
    return pow(pow(dst_x-src_x, 2)+pow(dst_y-src_y, 2), 1/2)

def solve():
    st_pt_ancestors = set() # start point's ancestor
    ed_pt_ancestors = set()
    x1,y1,x2,y2 = map(int, input().split())
    N = int(input())
    for n in range(N):
        cx,cy,r = map(int,input().split())
        if euclidean_dist(x1,y1,cx,cy) < r:
            st_pt_ancestors.add(n)
        if euclidean_dist(x2,y2,cx,cy) < r:
            ed_pt_ancestors.add(n)
    ans = len(st_pt_ancestors ^ ed_pt_ancestors)
    print(ans)

if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        solve()