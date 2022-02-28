import sys
from fractions import Fraction as frac

MOD = int(1e9+7)

def make_pascal(max_k):
    # https://ko.wikipedia.org/wiki/파스칼의_삼각형
    global P
    P = []
    for n in range(max_k+1):
        P.append([frac(0)]*(max_k+1))
        P[n][0] = frac(1)
        for k in range(1,n+1):
            P[n][k] = P[n-1][k-1]+P[n-1][k]

def make_G(): # inverts P matrix
    global P, G
    # Cut unnecessary part from P & Create I matrix (I=G)
    P = [[P[y][x] if x < y else frac(0) for x in range(len(P)-1)] for y in range(1,len(P))]
    P = [[-P[y][x] if (x+y)%2 else P[y][x] for x in range(len(P))] for y in range(len(P))]
    G = [[frac(1) if x == y else frac(0) for x in range(len(P))] for y in range(len(P))]
    # Make RREF on P while P is augmented -> P:I
    def Ei(i,s):
        for x in range(len(P)):
            P[i][x] = s * P[i][x]
            G[i][x] = s * G[i][x]
    def Eij(i,j,s):
        for x in range(len(P)):
            P[j][x] += s * P[i][x]
            G[j][x] += s * G[i][x]
    for i in range(len(P)): # REF
        if P[i][i] == 0: continue
        if P[i][i] != 1: Ei(i,frac(1,P[i][i]))
        for j in range(i+1,len(P)):
            Eij(i,j,frac(-P[j][i],1))
    for i in range(len(P)-1,-1,-1): # RREF
        if P[i][i] == 0: continue
        if P[i][i] != 1: Ei(i,frac(1,P[i][i]))
        for j in range(i-1,-1,-1):
            Eij(i,j,frac(-P[j][i],1))


def imul(a:int, b:int):
    return (a*b) % MOD

def ipow(base:int, power:int):
    ret, piv = 1, base
    while power:
        if (power & 1):
            ret = imul(ret, piv)
        piv = imul(piv, piv)
        power >>= 1
    return ret

def testcase():
    """ Faulhaber's formula,
    https://en.wikipedia.org/wiki/Faulhaber%27s_formula#From_examples_to_matrix_theorem
    행렬을 이용한 항목에 대해, 다항식 계수의 역행렬 G를 구하고 \Sigma{_x=1^N}x^k 와 내적한다. """
    N, K = map(int, sys.stdin.readline().split())
    make_pascal(K+1)
    make_G()
    # Modded Dot Product
    rem = 0
    for k,g in enumerate(G[K]):
        # G[i]가 1일 때, 불필요한 연산 생략
        if g: rem += imul(N**(k+1), g)
    return rem % MOD

if __name__ == '__main__':
    T = 1
    for t in range(T):
        ans = testcase()
        print(ans)