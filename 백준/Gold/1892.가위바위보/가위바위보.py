import sys
import fractions

MAX_N = 40
MAX_K = 40

def make_pascal(x): # 파스칼 삼각형(P) 생성
    global P
    P = [[1],[1,1]]
    for n in range(2,x):
        row = [1]+[P[n-1][k-1]+P[n-1][k] for k in range(1,n)]+[1]
        P.append(row)

def testcase():
    N, K = map(int, sys.stdin.readline().split())
    make_pascal(41)
    # n: 승부가 나기 직전까지의 판 수
    # k: 동주가 이긴 횟수: 0 ~ K-1
    ans = fractions.Fraction(0)
    P[40][40]
    for n in range(K-1, N):
        for k in range(min(K,n-(K-1)+1)):
            ans += fractions.Fraction(P[n][K-1]*P[n-(K-1)][k], 3**(n+1))
    print(f'{ans.numerator} {ans.denominator}')

if __name__ == '__main__':
    testcase()