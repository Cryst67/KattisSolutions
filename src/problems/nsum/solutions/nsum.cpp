#include <iostream>
#include <string>
#include <vector>
using namespace std;
int main(){
    int n; cin >> n;
    vector<int> v;
    for (size_t i = 0; i < n; i++){
        int t; cin >> t;
        v.push_back(t);
    }
    int sum = 0;
    for(auto i: v){
        sum += i;
    }
    cout << sum << '\n';
}
