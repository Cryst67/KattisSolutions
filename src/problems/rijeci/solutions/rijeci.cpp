#include <iostream>
#include <utility>
using namespace std;

int main(){

    std::pair<int,int> ab{1,0};
    int n; cin >> n;
    for(auto i = 0; i < n; i++){
        int temp = ab.first;
        int temp2 = ab.second;
        ab.first = 0;
        ab.second+= temp;
        ab.first += temp2;
    }

    cout << ab.first << ' ' << ab.second << '\n';
    return 0;
}