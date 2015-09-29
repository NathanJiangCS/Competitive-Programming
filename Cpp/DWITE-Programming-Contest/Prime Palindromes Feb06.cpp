#include <cstdio>
#include <string>
#include <sstream>
using namespace std;
string reverse(string s)
{
    string result = "";
    for (int i=0; i<s.length(); i++){
        result = s[i] + result;
    }
    return result;
}
int main()
{
    for (int zx=0; zx < 5; zx++){

        int n,m;
        int c=0;
        scanf("%d %d", &n, &m);
        bool mul[m+1];
        for (int i = 0; i<m+1; i++){
            mul[i] = true;
        }
        for (int i=2; i<m+1; i++){
            if (mul[i] == true){
                for (int j = 2*i; j<m+1; j+=i){
                    mul[j] = false;
                }
                string text = to_string(i);
                string textr = reverse(text);
                if (text == textr && n <= i && i <= m){
                    c += 1;
                }
            }

        }
        printf("%d\n", c);

    }
    return 0;
}
