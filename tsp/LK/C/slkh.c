// Simplified Lin-Kernighan Heuristic
#define W(i,j) Dist[Path[i]][Path[j]]

#include <stdlib.h>;

void Reverse(int *bgn, int *end) {
    while (bgn < end) {
        int tmp = *bgn;
        *bgn++ = *end;
        *end-- = tmp;
    }
}

int ImprovePath(int Path[], int N, int depth, int Restricted[], int PathOut[]) {
    int fImp;
    int gmin = N >= 10000 ? -originalLength/N/4 : -originalLength/N/2;
    if (depth < ALPHA) {
        for (int j = 0; j < N-1; j++) {
            int i = (j + Bgn[depth]) % (N-1);   // i = 0 ～ N-2
            int nid = Path[i];
            if (!Restricted[nid]) {
                int g = W(i,i+1) - W(N-1,i);  // 距離減少量
                if (g > gmin) {
                    sumInc += W(i+1,0) - W(N-1,0) - g;
                    Reverse(&Path[i+1], &Path[N-1]);  // #i+1 から #N-1 の経路を逆順に並び替える
                    if (sumInc < 0) {
                        memcpy(PathOut, Path, N*sizeof(int));
                        printf("%d#%d,\t\t\t \r", depth, originalLength + sumInc);
                        return 1;  // PathOutに書き込んだ
                    }
                    // 巡回経路の距離が改善しなかったケース
                    Restricted[nid] = 1;
                    fImp = ImprovePath(Path, N, depth+1, Restricted, PathOut);
                    Restricted[nid] = 0;
                    if (fImp) return 1;
                }
            }
            Bgn[depth] = (Bgn[depth] + 1) % (N-1);
        }
    } else {
        int i = 0, g = INT_MIN;
        for (int j = 0; j < N-1; j++) {
            int h = W(j,j+1) - W(N-1,j);            // 距離減少量
            if (h > g) {
                g = h;                              // 最大値を求める
                i = j;                              // このときの添え字
            }
        }
        if (g > 0) {
            int nid = Path[i];
            sumInc += W(i+1,0) - W(N-1,0) - g;
            Reverse(&Path[i+1], &Path[N-1]);        // 部分パス(i+1～N-1)を逆順に並び替え
            if (sumInc < 0) {
                memcpy(PathOut, Path, N*sizeof(int));
                printf("%d$%d,\r", depth, originalLength+sumInc);
                return 1;
            }
            Restricted[nid] = 1;
            fImp = ImprovePath(Path, N, depth+1, Restricted, PathOut);
            Restricted[nid] = 0;
            if (fImp) return 1;
        }
    }
    return 0;
}

void SimplifiedLKH(int Tour[], int NodeNum) {
    for (int i = 0; i++ < NodeNum; Bgn[0] = (Bgn[0]+1) % NodeNum) {
        originalLength = TourLength(Tour, NodeNum);
        sumInc = 0;
        if (i%100==0) printf("i0=%d;i=%d: %d,\r", Bgn[0], i, originalLength);
        memcpy(PathIn, &Tour[Bgn[0]], (NodeNum-Bgn[0])*sizeof(int));
        memcpy(&PathIn[NodeNum-Bgn[0]], Tour, Bgn[0]*sizeof(int));
        if (ImprovePath(PathIn, NodeNum, 1, Restricted, Tour)) {
            i = 0;
        }
    }
}