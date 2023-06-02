#include <iostream>
#include <string>
#include <vector>
using namespace std;
int main(){
    int n;
    cin >> n;
    vector<string> v;
    for(int i = 0; i < n; i++){
        string s;
        cin >> s;
        v.push_back(s);
    }
    for (size_t i = 0; i < n; i++){
        int index = i + 1;
        if (index % 2 == 0) continue;
        cout << v[i] << '\n';
    }
    
}