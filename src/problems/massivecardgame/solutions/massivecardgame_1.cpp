#include <algorithm>
#include <iostream>
#include <utility>
#include <vector>
using namespace std;

int lowerBound(vector<int>&, int);

auto main() -> int {
    int n; cin >> n;
    vector<int> v;
    for(int i = 0; i < n; i++){
        int a; cin >> a;
        v.push_back(a);
    }
    sort(v.begin(), v.end());
    int m; cin >> m;
    vector<pair<int,int>> ranges;
    for(int i = 0; i < m; i++){
        int l, r; cin >> l >> r;
        pair<int, int> p = {l, r};
        ranges.push_back(p);
    }
    for(auto p: ranges){
        int l = p.first;
        int r = p.second;
        cout << lowerBound(v, r + 1) - lowerBound(v, l) << '\n';
    }
    return 0;
}

int lowerBound(vector<int>& v, int tgt){
    int lo = -1; int hi = v.size();
    while(lo + 1 < hi){
        int mid = (lo + hi)/2;
        if(v[mid] >= tgt){
            hi = mid;
            continue;
        }
        lo = mid;
    }
    return hi;
}