#include <math.h>
#include <stdio.h>
#include <stdlib.h>                         // INT_MAX, _MAX_PATH
#include <string.h>
#include <time.h>                           // clock()

#define  MAX_NODENUM      14000             // 最大ノード数
#define  POPSIZE             50
#define  TOURNAMENTSIZE       6

typedef struct {
    int Nodes[MAX_NODENUM];                 // 経路格納配列
    int distance;                           // 巡回経路の総距離
} Tour;

const char *DATADIR = "C:\\LKHOptimizer\\TSPLIB";
int    NodeNum;                             // ノード数
double X[MAX_NODENUM], Y[MAX_NODENUM];      // X,　Y座標格納配列
int    Dist[MAX_NODENUM][MAX_NODENUM];      // 距離配列
int    Nodes[MAX_NODENUM];                  // 経路格納配列
int    NodeCount;                           // 現在の経路上のノード数(NI専用)
Tour   Tours[POPSIZE*2];                    // 経路群(現世代と次世代)(GA専用)
char   FlagPos[MAX_NODENUM], FlagId[MAX_NODENUM];
int    Curr = 0, Next = POPSIZE;            // 一世代ごとに交換

FILE *fopenex(const char *path, const char *mode) {
    FILE *fp = fopen(path, mode);
    if (fp == NULL) printf("ファイル %s がオープンできません\n", path);
    return fp;
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

void Swap(int *p, int *q) {
    int temp = *p;
    *p = *q;
    *q = temp;
}

void NearestNeighbor(int nodes[]) {
    for (int i = 0; i < NodeNum-2; i++) {
        int posmin, distmin = INT_MAX;
        for (int v = i+1; v < NodeNum; v++) {
            int dist = Dist[nodes[i]][nodes[v]];
            if (dist < distmin) {
                posmin = v;
                distmin = dist;
            }
        }
        Swap(&nodes[i+1], &nodes[posmin]);  // nodes[i]に一番近いものを nodes[i+1]に移動
    }
}

void InsertAt(int nodes[], int ix, int id) {
    memmove(&nodes[ix+1], &nodes[ix], sizeof(int)*(NodeCount-ix));
    nodes[ix] = id;  // Nodes[ix]以降を右(後)にずらし、空けたところに id をセットする
    NodeCount++;    // 拠点数が１つ増える
}   // ix == NodeCount のときは実際上移動はなく、末尾への追加となる

int NearestInsert(int nodes[], int insId) {
    int posmin, incmin = INT_MAX;
    for (int n = 1; n <= NodeCount; n++) {  // n の前に挿入
        int inc = Dist[nodes[n-1]][insId] + Dist[insId][nodes[n%NodeCount]] 
                                          - Dist[nodes[n-1]][nodes[n%NodeCount]];
        if (inc < incmin) {
            posmin = n;
            incmin = inc;
        }
    }
    InsertAt(nodes, posmin, insId);    // 最良位置(距離増分が最小)に挿入する
    return posmin;
}

// 経路の初期化は外部で行っておく
void NearestInsertion(int nodes[]) {
    NodeCount = 2;      // 初期ノードは二つ
    for (int n = NodeCount; n < NodeNum; n++) {
        NearestInsert(nodes, nodes[n]); // 順に距離増分が最小となる位置に挿入する
    }
}

// 乱数の初期化は外部で行う
void Shuffle(int array[], int size) {
    for(int i = 1; i < size; i++) {
        int j = rand()%size;
        int t = array[i];
        if (j == 0) continue;   // 先頭ノードは固定
        array[i] = array[j];
        array[j] = t;
    }
}

// 最良経路を得る
int getBestTourLength(Tour tours[], int *pixMin) {
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

// ランダムに TOURNAMENTSIZE個の経路を選びその中の最良のものを戻り値とする
int tournamentSelection() {
    int opttour, mindist = INT_MAX;
    for (int i = 0; i < TOURNAMENTSIZE; i++) {
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
                Swap(&Tours[Next+i].Nodes[k], &Tours[Next+i].Nodes[ix]);    // 交換
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
    return getBestTourLength(&Tours[Curr], NULL);
}

double elapsed(clock_t start) { return (double)(clock()-start)/CLOCKS_PER_SEC; }

void report(char *algo, int len, int optimum, clock_t start) {
    printf("%s距離: %d(%.2f) %.2f秒\n", algo, len, (double)len/optimum, elapsed(start));
}

int main(int argc, char *argv[]) {
    int n, num, length, optimum = 0;
    char path[_MAX_PATH], head[16], buf[256], name[64], linebuf[256];
    FILE *fp;

    clock_t start = clock();
    sscanf(argv[1], "%[a-z]%d", head, &NodeNum);
    sprintf(name, "%s%d", head, NodeNum);
    if (!(fp = fopenex("C:\\mh\\www\\np\\tsp\\tsplib.opt", "r"))) return 1;
    while (fgets(linebuf, sizeof(linebuf), fp) != NULL) {
        if (sscanf(linebuf, "%s %d", buf, &length) < 2) break;
        if (strcmp(buf,name) == 0) { optimum = length; break; }
    }
    fclose(fp);
    if (NodeNum > MAX_NODENUM) {
        printf("ノード数(%d)が最大値(%d)を超えています\n", NodeNum, MAX_NODENUM);
        return 1;
    }
    sprintf(path, "%s\\%s", DATADIR, argv[1]);
    if (!(fp = fopenex(path,"r"))) return 1;
    while (fgets(buf,sizeof(buf),fp) != NULL && strstr(buf,"NODE_COORD_SECTION") == NULL) ;
    for (n = 0; n < NodeNum && fscanf(fp, "%d %lf %lf\n", &num, &X[n], &Y[n]) == 3; n++) ;
    fclose(fp);
    if (n < NodeNum) { printf("データが不正です"); return 1; }
    CalcDistance();     // ノード間距離を Dist[][] にセットする
    printf("%s の最適解: %d 前処理 %.02f秒\n", name, optimum, elapsed(start));

    // Nearest Neighbor
    start = clock();
    for (n = 0; n < NodeNum; n++) Nodes[n] = n;  // 経路の初期化
    NearestNeighbor(Nodes);
    report("NN", TourLength(Nodes,NodeNum), optimum, start);

    // Nearest Insertion
    start = clock();
    for (n = 0; n < NodeNum; n++) Nodes[n] = n;  // 経路の初期化
    NearestInsertion(Nodes);
    report("NI", TourLength(Nodes,NodeNum), optimum, start);

    // Genetic Algorithm
    start = clock();
    report("GA", GA(), optimum, start);

    return 0;
}