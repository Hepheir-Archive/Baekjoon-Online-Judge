#include <stdio.h>
#include <stdlib.h>

void init(int *pT, int **px, int **py);
int calcMinExec(int x, int y);

int main(void) {
    int T;

    int *x;
    int *y;


    init(&T, &x, &y);

    int minExec;

    for (int i = 0; i < T; i++) {
        minExec = calcMinExec(*(x + i), *(y + i));
        printf("%d\n", minExec);
    }

    return 0;
}

void init(int *pT, int **px, int **py) {
    scanf("%d", pT);

    *px = (int *) malloc(sizeof(int) * *pT);
    *py = (int *) malloc(sizeof(int) * *pT);

    for (int i = 0; i < *pT; i++) {
        scanf("%d %d", (*px + i), (*py + i));
    }
}

int calcMinExec(int x, int y) {
    int d; // distance between x and y.

    d = y - x;

    if (d == 0) {
        return 0;
    }

    int chartLength;

    chartLength = 0;

    int i, j;
    int max_k;

    max_k = 1;

    for (i = 0; d > (max_k * 2); i++) {
        chartLength += 2;
        
        d -= (max_k * 2);

        max_k++;
    }

    // 원콤 해결 가능
    if (d <= max_k) {
        chartLength += 1;
    }

    // 원콤해결 불가능
    else {
        // Part 'd' into 2 integers : d1 and d2, 'd1' >= 'd2'.
        int d1 = (d % 2 == 0) ? d / 2 : d - (d / 2);
        int d2 = d - d1;

        chartLength += 2;
    }

    return chartLength;
}