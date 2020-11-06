#include <io.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

const char *DIR = "C:\\Users\\owner\\Desktop\\test\\ALL_tsp";
int    NodeNum;
double *X, *Y;      // 座標データ配列
int    *Tour;       // ツアー配列

int loaddata(char *path) {
    int  n, num;
    int  fEUC_2D = 0;
    char buf[256];
    FILE *fp = fopen(path, "r");

    while (fgets(buf, sizeof(buf), fp) != NULL) {
        if (strstr(buf,"EDGE_WEIGHT_TYPE") != NULL && strstr(buf,"EUC_2D") != NULL) {
            fEUC_2D = 1;
        } else if (strstr(buf, "NODE_COORD_SECTION") != NULL) {
            break;
        }
    }
    if (fEUC_2D == 0) {
        fclose(fp);
        return 0;   // ファイルタイプが EUC_2D ではない
    }
    X = (double*)calloc(NodeNum, sizeof(double));
    Y = (double*)calloc(NodeNum, sizeof(double));
    Tour = (int*)calloc(NodeNum, sizeof(int));
    if (X != NULL && Y != NULL && Tour != NULL) {
        for (n = 0; fscanf(fp, "%d %lf %lf", &num, &X[n], &Y[n]) == 3; n++) ;
    } else {
        printf("%s のメモリが確保できません\n", path);
    }
    fclose(fp);
    return (X != NULL && Y != NULL && Tour != NULL);
}

int loadtour(char *path) {
    int  n, length;
    char buf[256], *p;

    FILE *fp = fopen(path, "r");
    if (fp == NULL) return -1;
    while (fgets(buf, sizeof(buf), fp) != NULL) {
        if ((p = strstr(buf,"Length")) != NULL) {
            for (p += 6; !isdigit(*p); p++) ;
            length = atoi(p);
        } else if (strstr(buf, "TOUR_SECTION") != NULL) {
            break;
        }
    }
    for (n = 0; n < NodeNum && fscanf(fp, "%d\n", &Tour[n]) == 1; n++) ; 
    fclose(fp);
    return length;
}

int dist(int id1, int id2) {
    double xdif = X[id2] - X[id1];
    double ydif = Y[id2] - Y[id1];
    return (int)(sqrt(xdif*xdif + ydif*ydif) + 0.5);    // 四捨五入
}

int tourlength() {
    int length = 0;
    for (int i = 0; i < NodeNum; i++) {
        length += dist(Tour[i]-1, Tour[(i+1)%NodeNum]-1);
    }
    return length;
}

int main (int argc, char *argv[]) {
    char path[_MAX_PATH], pathTour[_MAX_PATH], head[16];
    struct _finddata_t fdata;
    intptr_t fh;
    int n = 1, lenOpt; 

    sprintf(path, "%s\\*.tsp", DIR);
    if ((fh = _findfirst(path,&fdata)) == -1) return 1;

    do {
        if ((fdata.attrib & _A_SUBDIR) == 0) {   
            sprintf(path, "%s\\%s", DIR, fdata.name);
            sscanf(fdata.name, "%[^0-9]%d", head, &NodeNum);
            if (loaddata(path) == 0) continue; 
            sprintf(pathTour, "%s\\%s%d.opt.tour", DIR, head, NodeNum);
            if ((lenOpt = loadtour(pathTour)) > 0) {
                printf("%d: %s %d len = %d : %d\n", 
                        n++, path, NodeNum, lenOpt, tourlength());
            }
            if (X != NULL) free(X);
            if (Y != NULL) free(Y);
            if (Tour != NULL) free(Tour);
        }
    } while (_findnext(fh, &fdata) == 0);
    _findclose(fh);
    return 0;
}