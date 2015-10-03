#include <cstdio>
#include <iostream>
using namespace std;

int main()
{
    int n, k;
    scanf("%i %i",&n,&k);
    int presum [n+1];
    presum[0] = 0;
    int m = 0;
    for (int i=0;i<n;i++){
        int c;
        scanf("%i", &c);
        m += c;
        presum[i+1] = m;
    }
    int largest = 0;
    for (int i=k; i<n+1; i++ ){
        m = presum[i] - presum[i-k];
        if (m>largest){
            largest = m;
        }
    }
    cout << largest << endl;
    return 0;
}
