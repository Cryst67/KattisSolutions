#include <iostream>
#include <vector>
#include <map>
using namespace std;

auto main() -> int {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    int n ,q; cin >> n >> q;
    map<int, int> m;
    for(int i = 0; i < n; i++){
        int d; cin >> d;
        if(m.count(d)) m[d] += 1;
        else m[d] = 1;
    }
    for (size_t i = 0; i < q; i++)
    {
        int t, d; cin >> t >> d;
        if(m.empty()){
            cout << -1 << '\n';
        }
        else if(t == 1){
            auto hi = m.upper_bound(d);
            if(hi == m.end()){
                cout << - 1 << '\n';
            }
            else{
                cout << hi->first << '\n';
                hi->second -= 1;
                if(hi->second == 0) m.erase(hi->first);
            }
        }
        else if(t == 2){
            auto lo = m.lower_bound(d);
            if(lo->first <= d && lo != m.end()) lo = lo;
            else if(lo != m.begin() || lo == m.end()) lo = prev(lo);
            if(lo->first <= d){
                cout << lo->first << '\n';
                lo->second -= 1;
                if(lo->second < 1) m.erase(lo->first);
            }else { 
                cout << -1 << '\n';
            }
        }
    }
    
    return 0;
}