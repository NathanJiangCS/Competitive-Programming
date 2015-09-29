#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <cstring>

using namespace std;

int main()
{
    int m,n,k;
    scanf("%d%d%d", &m, &n, &k);
    int grid[m+10][n+10]; memset(grid, 0, sizeof grid);

    for (int zxc = 0; zxc < k; zxc++){
        int x,y,r,b, topy, lowy;
        scanf("%d%d%d%d", &x, &y, &r, &b);
        lowy = y-r; topy = y+r;
        if (lowy <= 0){
            lowy = 1;
        }
        if (topy > m){
            topy = m;
        }
        for (int i = lowy; i <= topy; i++){
            int lowx, topx;
            double shift;
            shift = floor(sqrt(r*r - (y-i)*(y-i)));
            lowx = x - shift; topx = x + shift;
            if (lowx <= 0){
                lowx = 1;
            }
            if (topx > n){
                topx = n;
            }
            grid[i][lowx] += b; grid[i][topx+1] -= b;

            }
        }
    int mb = 0; int c = 0;
    for (int i = 1; i <= m; i++ ){
        for (int j=1; j<=n; j++){
            grid[i][j] += grid[i][j-1];
        }
    }
    for (int i = 0; i <= m; i++){
        for (int j = 0; j <= n; j++){
            if (grid[i][j] > mb){
                mb = grid[i][j];
                c = 1;
            }
            else if (grid[i][j] == mb){
                c += 1;
            }
        }
    }
    cout << mb << endl;
    cout << c << endl;
    return 0;
}
