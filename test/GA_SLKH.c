// cl \mh\www\np\tsp\tsp4.c
// gcc -o tsp4.exe -std=c99 \mh\www\np\tsp\tsp4.c
#include <math.h>                           // sqrt
#include <stdio.h>
#include <string.h>
#include <time.h>                           // clock()
#include <limits.h>                         // INT_MAX, _MAX_PATH
#include <windows.h>                        // 名前付きパイプによるプロセス間通信

#define D(n,m)  Dist[Tour[(n)%N]][Tour[(m)%N]]
#define SWAP(A,i,j) { int temp = A[i]; A[i] = A[j]; A[j] = temp; }
#define MAX_NODENUM    14000               // 最大ノード数
#define  POPSIZE             50
#define  TOURNAMENTSIZE       6

typedef struct {
    int Nodes[MAX_NODENUM];                 // 経路格納配列
    int distance;                           // 巡回経路の総距離
} GATour;

const char *DataDir = "C:\\Users\\imada\\Desktop\\Research\\test\\ALL_tsp";
int    NodeNum;                             // ノード数
int    NodeCount;                           // 現在の経路上のノード数(NI専用)
double X[MAX_NODENUM], Y[MAX_NODENUM];      // X, Y座標格納配列
int    Dist[MAX_NODENUM][MAX_NODENUM];      // 距離配列
int    Tour[MAX_NODENUM];                   // 経路格納配列
int    BestTour[MAX_NODENUM];               // Best経路格納配列
int    NewTour[MAX_NODENUM];                // 3-opt経路格納配列
int    Restricted[MAX_NODENUM];             // Simple LKH用フラグ配列
int    PathIn[MAX_NODENUM];
GATour  Tours[POPSIZE*2];                    // 経路群(現世代と次世代)(GA専用)
char   FlagPos[MAX_NODENUM], FlagId[MAX_NODENUM];
int    Curr = 0, Next = POPSIZE;            // 一世代ごとに交換

FILE *fopenex(const char *path, const char *mode) {
    FILE *fp = fopen(path, mode);
    if (fp == NULL) printf("ファイル %s がオープンできません\n", path);
    return fp;
}

void GA_Swap(int *p, int *q) {
    int temp = *p;
    *p = *q;
    *q = temp;
}

void CalcDistance() {
    for (int i = 0; i < NodeNum; i++) {
        for (int j = 0; j < i; j++) {
            double xdif = X[i] - X[j];
            double ydif = Y[i] - Y[j];
            Dist[j][i] = Dist[i][j] = (int)(sqrt(xdif*xdif + ydif*ydif) + 0.5);
        }   // Dist[i][i] = 0 は元々 Dist配列がゼロクリアされているため、省略する
    }
}

int TourLength(int nodes[], int num) {
    int length = 0;
    for (int i = 0; i < num; i++) {
        length += Dist[nodes[i]][nodes[(i+1)%num]];
    }
    return length;
}

void NearestNeighbor() {
    for (int i = 0; i < NodeNum-2; i++) {
        int posmin, distmin = INT_MAX;
        for (int v = i+1; v < NodeNum; v++) {
            int dist = Dist[Tour[i]][Tour[v]];
            if (dist < distmin) {
                posmin = v;
                distmin = dist;
            }
        }
        SWAP(Tour, i+1, posmin);
    }
}

void RemoveBlockAt(int ix, int n) {
    memmove(&Tour[ix], &Tour[ix+n], sizeof(int)*(NodeCount-n-ix));
    NodeCount -= n;
}

void InsertBlockAt(int nodes[], int ix, int ids[], int n) {
    memmove(&nodes[ix+n], &nodes[ix], sizeof(int)*(NodeCount-ix)); // 右(後)にずらし、
    memmove(&nodes[ix], ids, sizeof(int)*n); // 空けたところに ids[] をセットする
    NodeCount += n;    
}   // ix == NodeCount のときは実際上移動はなく、末尾への追加となる

int NearestInsertBlock(int nodes[], int insIds[], int k, int orgPos) {
    int posmin, incmin = INT_MAX;
    for (int n = 1; n <= NodeCount; n++) {  // n の前に挿入
        int inc = Dist[nodes[n-1]][insIds[0]] + Dist[insIds[k-1]][nodes[n%NodeCount]] 
                                              - Dist[nodes[n-1]][nodes[n%NodeCount]];
        if (n==orgPos ? inc <= incmin : inc < incmin) {
            posmin = n;
            incmin = inc;
        }
    }
    InsertBlockAt(nodes, posmin, insIds, k);    // 最良位置(距離増分が最小)に挿入する
    return posmin;
}

int NearestInsert(int nodes[], int insId, int orgPos) {
    return NearestInsertBlock(nodes, &insId, 1, orgPos);
}

void NearestInsertion(int nodes[]) {
    NodeCount = 2;      // 初期ノードは二つ
    for (int n = NodeCount; n < NodeNum; n++) {
        NearestInsert(nodes, nodes[n], -1); // 順に距離増分が最小となる位置に挿入する
    }
}

void Shuffle(int array[], int size) {   // array[0]は固定、array[1]以降をランダマイズする
    for(int i = 1; i < size; i++) {     // 先頭は固定
        int j = rand()%(size-1) + 1;    // 1 ～ size-1 (array[0]は固定)
        SWAP(array, i, j);
    }
}

void CheckNodeID(int Tour[], int Num) {
    for (int j, i = 0; i < Num; i++) {
        for (j = 0; j < Num && Tour[j] != i; j++) ;
        if (j == Num) printf("ノードID: %d がありません\n", i);
    }
}

void TwoOpt(int Tour[], int N) {
    for (int fImproved = 1; fImproved; ) {
        fImproved = 0;
        for (int i = 0; i < N-1; i++) {
            for (int j = i+1; j < N; j++) {
                if (D(i,j) + D(i+1,j+1) < D(i,i+1) + D(j,j+1)) {
                    for (int k = 0; k < (j-i)/2; k++) {
                        SWAP(Tour, i+1+k, j-k); // 部分経路を逆順に並び替える
                    }
                    fImproved = 1;   // 改善した
                }
            }
        }
    }
}

void RevCpy(int NewTour[], int Tour[], int N, int dst, int src, int num) {
    for (int n = 0; n < num; n++) {
        NewTour[(dst+n)%N] = Tour[(src-n)%N];   // 逆順にコピー
    }
}

void OrOpt(int Tour[], int N) {    // 部分経路長：1 ～ 5
    int insIds[5], newPos, beforeLength, length;
    NodeCount = N;
    for (int k = 1; k <= 5; ) {
        for (int n = 1; n <= N-k; ) {      // 先頭ノードは固定する
            for (int j = 0; j < k; j++) 
                insIds[j] = Tour[n+j];     // 移動候補
            RemoveBlockAt(n, k);           // 一旦削除する
            newPos = NearestInsertBlock(Tour, insIds, k, n); // 最良位置に挿入する
            if (newPos <= n) n++;
        }
        length = TourLength(Tour,N);
        if (k == 1 || length == beforeLength) k++;
        beforeLength = length;
    }
}

void ThreeOpt(int Tour[], int N) {
    for (int step = 1, fImproved = 1; fImproved; step++) {
        int length, Repeat = N*N;
        TwoOpt(Tour, N);
        OrOpt(Tour, N);
        length = TourLength(Tour,N);
        fImproved = 0;
        for (int cnt = 0; cnt < Repeat; cnt++) {
            int d[5], min = 0;
            int i = rand()%(N-2);
            int j = (i+1) + rand()%(N-2-i);
            int k = (j+1) + rand()%(N-1-j);
            d[0] = D(i,i+1) + D(j,j+1) + D(k,k+1);  // 元の距離
            d[1] = D(i,k) + D(j+1,i+1) + D(k+1,j);
            d[2] = D(j+1,i) + D(k,j) + D(k+1,i+1);
            d[3] = D(j,k+1) + D(i,j+1) + D(k,i+1);
            d[4] = D(i,j) + D(j+1,k+1) + D(k,i+1);
            for (int m = 1; m <= 4; m++) {
                if (d[m] < d[min]) min = m;    // ４通りのつなぎ替えを比較
            }
            if (min == 0) continue;
            memcpy(&NewTour[0], &Tour[i+1], (j-i)*sizeof(int)); // i+1～j
            if (min == 1) { // D(i,k) + D(j+1,i+1) + D(k+1,j)
                memcpy(&NewTour[j-i], &Tour[k+1], (N-k-1)*sizeof(int)); // k+1～N
                memcpy(&NewTour[j-i+N-k-1], &Tour[0], (i+1)*sizeof(int));   // 0～i
                RevCpy(NewTour, Tour, N, (j+N-k)%N, k, k-j);    // k～j+1
            } else if (min == 2) { // D(j+1,i) + D(k,j) + D(k+1,i+1);
                RevCpy(NewTour, Tour, N, j-i, k, k-j);  // k～j+1
                RevCpy(NewTour, Tour, N, k-i, N+i, N+i-k);  // k+1～i
            } else if (min == 3) { // D(j,k+1) + D(i,j+1) + D(k,i+1)
                memcpy(&NewTour[j-i], &Tour[k+1], (N-k-1)*sizeof(int)); // k+1～N
                memcpy(&NewTour[j-i+N-k-1], &Tour[0], (i+1)*sizeof(int));   // 0～i
                memcpy(&NewTour[j+N-k], &Tour[j+1], (k-j)*sizeof(int)); // j+1～k
            } else if (min == 4) { // D(i,j) + D(j+1,k+1) + D(k,i+1)
                RevCpy(NewTour, Tour, N, j-i, N+i, N+i-k);  // k+1～i
                memcpy(&NewTour[j+N-k], &Tour[j+1], (k-j)*sizeof(int)); // j+1～k
            }
            memcpy(Tour, NewTour, N*sizeof(int));
            fImproved = 1;
            cnt = 0;
        }
    }
}

// Simplified Lin-Kernighan Heuristic
#define ALPHA              5               // Simple LKH の深さ制限
#define W(i,j) Dist[Path[i]][Path[j]]
int originalLength, sumInc;

int ImprovePath(int Path[], int N, int depth, int Restricted[], int PathOut[]) {
    int fImp;
    if (depth < ALPHA) {
        for (int i = 0; i < N-1; i++) {
            int nid = Path[i];
            if (!Restricted[nid]) {
                int g = W(i,i+1) - W(N-1,i);  // 距離減少量
                if (g > -originalLength/N/2) {
                    sumInc += W(i+1,0) - W(N-1,0) - g;
                    for (int k = 0; k < (N-i-1)/2; k++) {
                        SWAP(Path, i+1+k, N-1-k);
                    }   // #i+1 から #N-1 の経路を逆順に並び替える
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
        }
    } else {		// } else if (depth < ALPHA*2) {
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
            for (int k = 0; k < (N-i-1)/2; k++) {
                SWAP(Path, i+1+k, N-1-k);           // 部分パス(i+1～N-1)を逆順に並び替え
            }
            if (sumInc < 0) {
                memcpy(PathOut, Path, N*sizeof(int));
                printf("%d$%d\r", depth, originalLength+sumInc);
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
    for (int i0 = 0, i = 0; i++ < NodeNum; i0 = (i0+1) % NodeNum) {
        originalLength = TourLength(Tour, NodeNum);
        sumInc = 0;
        if (i%100==0) printf("i0=%d;i=%d: %d\r", i0, i, originalLength);
        memcpy(PathIn, &Tour[i0], (NodeNum-i0)*sizeof(int));
        memcpy(&PathIn[NodeNum-i0], Tour, i0*sizeof(int));
        if (ImprovePath(PathIn, NodeNum, 1, Restricted, Tour)) {
            i = 0;
        }
    }
}

double elapsed(clock_t start) { return (double)(clock()-start)/CLOCKS_PER_SEC; }

void Report(char *algo, int len, int optimum, clock_t start) {
    printf("%s: %d(%.4f) %.2f[s]\n", algo, len, (double)len/optimum, elapsed(start));
}

void SendData(void *pData, int size) {
    DWORD dwBytesWritten; 
    HANDLE hPipe = CreateFile("\\\\.\\pipe\\tspviewer", GENERIC_READ | GENERIC_WRITE, 
                0, NULL, OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, NULL);
    if (hPipe == INVALID_HANDLE_VALUE) return;
    WriteFile(hPipe, pData, size, &dwBytesWritten, NULL);
    CloseHandle(hPipe);
    Sleep(100);
}

void SendCommand(char *cmd, char *param1, char *param2) {
    char  buf[256];
    sprintf(buf, "%s %s%s", cmd, param1, param2);
    SendData(buf, strlen(buf));
}


//GA用関数
int getBestTourLength(GATour tours[], int *pixMin) {
    int minDistance = INT_MAX;
    for (int i = 0; i < POPSIZE; i++) {
        tours[i].distance = TourLength(tours[i].Nodes, NodeNum);
        if (tours[i].distance < minDistance) {
            if (pixMin != NULL) *pixMin = i;
            minDistance = tours[i].distance;
        }
    }
    return minDistance;
}

void getBestTour(GATour tours[], int* min_tour ,int* min_ind) {
    int minDistance = INT_MAX;
    for (int i = 0; i < POPSIZE; i++) {
        if (tours[i].distance < minDistance) {
            minDistance = tours[i].distance;
            *min_ind = i;
            memcpy(min_tour,tours[i].Nodes,sizeof(tours[i].Nodes));
        }
    }
}

// ランダムに TOURNAMENTSIZE個の経路を選びその中の最良のものを戻り値とする
int tournamentSelection() {
    int opttour, mindist = INT_MAX;
    for (int i = 0; i < TOURNAMENTSIZE; i++) {
//        int ix = (rand() % (POPSIZE-1)) + 1;
        int ix = rand() % POPSIZE;
        if (Tours[Curr+ix].distance < mindist) {
            opttour = ix;
            mindist = Tours[Curr+ix].distance;
        }
    }
    return opttour;
}

// １世代進める
void evolvePopulation(int ixBest) {
    Tours[Next+0] = Tours[Curr+ixBest];       // 最良経路はそのまま残す

    // 交差で新経路を生成する
    for (int i = 1; i < POPSIZE; ) {
        int parent1, parent2;
        int bgnPos = rand() % NodeNum;
        int endPos = rand() % NodeNum;
        if (bgnPos > endPos) continue;
        memset(FlagPos, 0, sizeof(FlagPos));    // フラグ配列をゼロクリア
        memset(FlagId, 0, sizeof(FlagId));
        parent1 = tournamentSelection();
        parent2 = tournamentSelection();
//      if (parent1 == parent2) continue;
//printf("%d %d\n", parent1, parent2);
        for (int k = bgnPos; k <= endPos; k++) {
            int id = Tours[Curr+parent1].Nodes[k];
            Tours[Next+i].Nodes[k] = id;
            FlagPos[k] = 1;
            FlagId[id] = 1;
        }
        for (int m = 0, k = 0; k < NodeNum; k++) {
            int id = Tours[Curr+parent2].Nodes[k];
            if (FlagId[id] == 1) continue;      // 登録済み
            while (FlagPos[m] == 1) m++;        // 登録済みの場所は飛ばす
            FlagPos[m] = 1;                     // #m に登録する 
            FlagId[id] = 1;
            Tours[Next+i].Nodes[m++] = id;
        }

        // 突然変異
        for (int k = 1; k < NodeNum; k++) {
            if (rand()%10000 < 45) {
                int ix = (rand() % (NodeNum-1)) + 1;    // 1 ～ NodeNum-1
                GA_Swap(&Tours[Next+i].Nodes[k], &Tours[Next+i].Nodes[ix]);    // 交換
            }
        }

        i++;
    }
}

int GA() {
    // 初期経路群を生成する
    for (int n = 0; n < POPSIZE; n++) {
        for (int k = 0; k < NodeNum; k++)
            Tours[Curr+n].Nodes[k] = k;  // 初期経路 0, 1, ... , NodeNum-1
        srand(n * 111);              // 必要に応じて見直す
        Shuffle(Tours[Curr+n].Nodes, NodeNum);   // 初期経路をランダマイズ
        NearestInsertion(Tours[Curr+n].Nodes);
    }
    // 進化させる
    for (int j = 0; j < 2000; j++) {
        int ixBest;
        int minDistance = getBestTourLength(&Tours[Curr], &ixBest);
        if (j%100 == 0) printf("%d\t", minDistance);
        evolvePopulation(ixBest);   // Curr -> Next
        Curr = Next;                // 配列領域を現世代と次世代で入れ替える
        Next = POPSIZE - Curr;
    }
    printf("\n");
    return getBestTourLength(&Tours[Curr], NULL);
}

void Multi_Report(char *algo, int len, int optimum, clock_t start,int x) {
    printf("%d: %s length: %d(%.4f) %.2f[s]\n",x, algo, len, (double)len/optimum, elapsed(start));
}

int main(int argc, char *argv[]) {
    int n, k, num, length, minLength, optimum = 0, num1, num2;
    int min_tour[MAX_NODENUM];
    int ind,min_ind;
    char path[260], head[16], buf[256], name[64], linebuf[256];
    FILE *fp;
    clock_t start;

    if (strchr(argv[1], '-') == NULL) {
        sscanf(argv[1], "%[a-zA-Z]%d", head, &NodeNum);
        sprintf(name, "%s%d", head, NodeNum);
        sprintf(path, "%s\\%s", DataDir, argv[1]);
    } else {
        sscanf(argv[1], "%[a-zA-Z]%d-%d", head, &num1, &num2);
        NodeNum = num1 - num2;
        sprintf(name, "%s%d-%d", head, num1, num2);
        sprintf(path, "%s", argv[1]);
    }
    if (strchr(argv[1], '-') == NULL) {
        if (!(fp = fopenex("C:\\Users\\imada\\Desktop\\Research\\test\\ALL_tsp\\tsp_opt.txt", "r"))) return 1;
        while (fgets(linebuf, sizeof(linebuf), fp) != NULL) {
            if (sscanf(linebuf, "%s %d", buf, &length) < 2) break;
            if (strcmp(buf, name) == 0) { optimum = length; break; }
        }
        fclose(fp);
        printf("%s oprimum：%d\n", name, optimum);
    }
    if (NodeNum > MAX_NODENUM) {
        printf("ノード数(%d)が最大値(%d)を超えています\n", NodeNum, MAX_NODENUM);
        return 1;
    }
    if (!(fp = fopenex(path,"r"))) return 1;
    while (fgets(buf,sizeof(buf),fp) != NULL && strstr(buf,"NODE_COORD_SECTION") == NULL) ;
    for (n = 0; n < NodeNum && fscanf(fp, "%d %lf %lf\n", &num, &X[n], &Y[n]) == 3; n++) ;
    fclose(fp);
    if (n < NodeNum) { printf("データが不正です"); return 1; }
    CalcDistance();     // ノード間距離を Dist[][] にセットする

    SendCommand("load", path, "");

    start = clock();
    for (n = 0; n < NodeNum; n++) Tour[n] = n;  // 経路の初期化
    //SimplifiedLKH(Tour, NodeNum);
    //Report("S-LKH", TourLength(Tour,NodeNum), optimum, start);
    NearestNeighbor();
    Report("NN", TourLength(Tour,NodeNum), optimum, start);
/*
    minLength = INT_MAX;
    srand(9999);
    for (k = 0; k < 10; k++) {
		int nid = rand()%NodeNum;	// 先頭ノードに置き換えるノード
        for (n = 0; n < NodeNum; n++) Tour[n] = n;  // 経路の初期化
        SWAP(Tour, 0, nid);  // 先頭ノードをランダムにスワップ
        NearestNeighbor();
        TwoOpt(Tour, NodeNum);
        if ((length = TourLength(Tour,NodeNum)) < minLength) {
            minLength = length;
            memcpy(BestTour, Tour, sizeof(int)*NodeNum);
        }
    }
    memcpy(Tour, BestTour, sizeof(int)*NodeNum);

    Report("NN2opt*10", minLength, optimum, start);
    ThreeOpt(Tour, NodeNum);
    Report("NN2opt*10 3opt", TourLength(Tour,NodeNum), optimum, start);
*/
    SimplifiedLKH(Tour, NodeNum);
    Report("S-LKH", TourLength(Tour,NodeNum), optimum, start);

    SendData(Tour, NodeNum*sizeof(int));
    SendCommand("title", "NN2opt*10 (2opt ORopt 3opt)* S-LKH", "");
    SendCommand("savepng", name, "_nn2_2o3slkh.png");
    CheckNodeID(Tour, NodeNum);
    printf("\n");

    start = clock();
    for (n = 0; n < NodeNum; n++) Tour[n] = n;  // 経路の初期化
    NearestInsertion(Tour);
    Report("NI", TourLength(Tour,NodeNum), optimum, start);
    TwoOpt(Tour, NodeNum);
    Report("NI 2opt", TourLength(Tour,NodeNum), optimum, start);
    CheckNodeID(Tour, NodeNum);
    start = clock();
    minLength = INT_MAX;
    for (k = 0; k < 10; k++) {
        for (n = 0; n < NodeNum; n++) Tour[n] = n;  // 経路の初期化
        srand(k * 111);
        Shuffle(Tour, NodeNum);                     // 初期経路をランダマイズ
        NearestInsertion(Tour);
        if ((length = TourLength(Tour,NodeNum)) < minLength) {
            minLength = length;
            memcpy(BestTour, Tour, sizeof(int)*NodeNum);
        }
    }
    printf("\n");
    
    Report("NI*10", minLength, optimum, start);
    memcpy(Tour, BestTour, sizeof(int)*NodeNum);
    TwoOpt(Tour, NodeNum);
    Report("NI*10 2opt", TourLength(Tour,NodeNum), optimum, start);
    ThreeOpt(Tour, NodeNum);
    Report("NI*10 2opt 3opt", TourLength(Tour,NodeNum), optimum, start);
    //for (n = 0; n < NodeNum; n++) Tour[n] = n;  // 経路の初期化
    SimplifiedLKH(Tour, NodeNum);
    Report("S-LKH", TourLength(Tour,NodeNum), optimum, start);

    SendData(Tour, NodeNum*sizeof(int));
    CheckNodeID(Tour, NodeNum);
    SendCommand("title", "NI*10 (2opt ORopt 3opt)* S-LKH", "");
    SendCommand("savepng", name, "_ni10_2o3slkh.png");
    printf("\n");

    start = clock();
    Report("GA", GA(), optimum, start);
    getBestTour(Tours,min_tour,&min_ind);
    SimplifiedLKH(min_tour,NodeNum);
    Report("S-LKH", TourLength(min_tour,NodeNum), optimum, start);
    printf("\n");

    minLength = INT_MAX;
    for(int i = 0; i < POPSIZE; i++){
        SimplifiedLKH(Tours[i].Nodes,NodeNum);
        length = TourLength(Tours[i].Nodes,NodeNum);
        Multi_Report("GA-SLKH", length, optimum, start,i);
        if(length < minLength){
            minLength = length;
            ind = i;
        }
    }

    printf("min_ind : %d  length: %d\n",min_ind,TourLength(Tours[min_ind].Nodes,NodeNum));
    printf("best_ind: %d  length: %d\n",ind,minLength);
    //SimplifiedLKH(min_tour,NodeNum);
    //Report("S-LKH", TourLength(min_tour,NodeNum), optimum, start);

    return 0;
}