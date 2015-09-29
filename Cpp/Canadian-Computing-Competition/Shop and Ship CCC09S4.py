#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>
#include <iostream>

using namespace std;

int main()
{
    int n, t, x, y, c, k;
    scanf("%d", &n);
    vector<pair<int,int> > graph[n];
    scanf("%d", &t);
    for(int i=0; i<t; i++){
        scanf("%d %d %d", &x, &y, &c);
        x-=1;y-=1;
        graph[x].push_back(make_pair(y,c));
        graph[y].push_back(make_pair(x,c));
    }
    int mincost = 999999999;
    scanf("%d", &k);
    int cities[k][2];
    for (int i=0; i<k ; i++){
        int a,b;
        scanf("%d %d", &a, &b);
        a -= 1;
        cities[i][0] = a;
        cities[i][1] = b;

    }
    int dest, u;
    scanf("%d", &dest); dest -= 1;

    vector<int> dp; dp.assign(n, 900000001);
    queue <int> q;
    q.push(dest);
    dp[dest] = 0;

    while (q.size() > 0){
        u = q.front();
        q.pop();
        for (int i=0; i < graph[u].size(); i++ ){
            x = graph[u][i].first;
            y = graph[u][i].second;
            if (dp[x] > dp[u] + y){
                dp[x] = dp[u] + y;
                q.push(x);
            }
        }
    }

    for(int i =0; i<k; i++){
        int a,b;
        a = cities[i][0]; b = cities[i][1];
        if (dp[a]+b < mincost){
            mincost = dp[a] + b;

        }
    }
    printf("%d", mincost);
    return 0;
}
