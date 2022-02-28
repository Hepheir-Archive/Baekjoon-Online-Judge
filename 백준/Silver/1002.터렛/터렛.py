import sys
import math
input = sys.stdin.readline

def testcase():
    x1,y1,r1,x2,y2,r2 = map(int, input().split())
    dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    if dist == 0 and r1 == r2: # 일치
        print(-1)
    elif dist == r1+r2: # 외접
        print(1)
    elif abs(r1-r2) == dist: # 내접
        print(1)
    elif abs(r1-r2) > dist: # 안에 있음
        print(0)
    elif abs(r1-r2) < dist < r1+r2: # 곂침
        print(2)
    elif r1+r2 < dist: # 밖에 있음
        print(0)
    

if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        testcase()