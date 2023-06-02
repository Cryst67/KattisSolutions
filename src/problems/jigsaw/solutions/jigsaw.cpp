#include <iostream>
#include <utility>
#include <vector>
#include <math.h>
using namespace std;

void jigSaw(int c, int m, vector<pair<int, int>> vec);

int main(){
    int c, e, m; cin >> c >> e >> m;
    int num = c+e+m;
    vector<pair<int,int>> vec;
    for(int i = 2; i < sqrt(num)+1; i++){
        if(num%i == 0){
            pair <int,int> p;
            p.first = i;
            p.second = num/i;
            vec.push_back(p);
        }
    }
    jigSaw(c, e, vec);
    return 0;
}

void jigSaw(int c, int m, vector<pair<int, int>> vec){
    if(c != 4){
        cout << "impossible" << '\n';
        return;
    }
    for(auto i : vec){
        if(((i.first+i.second)*2 - 8) == m){
            cout << i.first << ' ' << i.second << '\n';
            return;
        }
    }
    cout << "impossible" << '\n';
}