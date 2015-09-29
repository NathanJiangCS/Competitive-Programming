#include <cstdio>
#include <vector>
#include <iostream>
#include <queue>

using namespace std;

int main ()
{
    int n, m, x, y, start, en, u;
    scanf("%d %d", &n, &m);


    vector<int>  taller[n];

    for (int i=0; i < m; i++) {

        scanf("%d %d", &x, &y);
        x -= 1; y -= 1;
        taller[x].push_back(y);

    }
    scanf("%d %d", &start, &en);
    start -= 1; en -= 1;
    vector<bool> flag; flag.assign(n, false);
    vector<int> dp; dp.assign(n, 1000001);

    queue<int> q;
    q.push(start); flag[start] = true; dp[start] = 0;

    while (q.size() > 0) {

        u = q.front();
        q.pop();
        for (int i = 0; i < taller[u].size(); i++){
            int next = taller[u][i];
            if (flag[next] == false) {

                flag[next] = true;
                dp[next] = dp[u] + 1;
                q.push(next);
            }

        }
    }
    if (dp[en] != 1000001){

        cout << "yes" << endl;
    }
    else {
        vector<bool> flag; flag.assign(n, false);
        vector<int> dp; dp.assign(n, 1000001);

        queue<int> q;
        q.push(en); flag[en] = true; dp[en] = 0;

        while (q.size() > 0) {

            u = q.front();
            q.pop();
            for (int i = 0; i < taller[u].size(); i++){
                int next = taller[u][i];
                if (flag[next] == false) {

                    flag[next] = true;
                    dp[next] = dp[u] + 1;
                    q.push(next);
                }

            }
        }
        if (dp[start] != 1000001) {
            cout << "no" << endl;
        }
        else {
            cout << "unknown" << endl;
        }
    }
    return 0;
}
