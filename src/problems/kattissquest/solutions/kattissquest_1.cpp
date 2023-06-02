#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <queue>
using namespace std;

auto main() -> int {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    map <int, priority_queue<int, vector<int>>> m;
    int n {}; cin >> n;
    for (size_t i = 0; i < n; i++) {
        string cmd; cin >> cmd;
        if(cmd == "add"){
            int e, g; cin >> e >> g;
            m[e].push(g);
        }
        if (cmd == "query") {
    int q;
    cin >> q;
    long long gold = 0;
    while (true) {
        if (m.empty() || q == 0) {
            cout << gold << '\n';
            break;
        }
        auto lb = m.lower_bound(q);

        bool no_suitable_key = false;
        if(lb == m.end()) {
            lb = prev(lb);
            if(lb->first > q) no_suitable_key = true;
        }
        else if (lb != m.begin()) {
            if (lb->first > q) {
                lb = prev(lb);
                if (lb->first > q) no_suitable_key = true;
            }
        } else {
            if (lb->first > q) no_suitable_key = true;
        }

        if (no_suitable_key) {
            cout << gold << '\n';
            break;
        }

        int g = lb->second.top();
        gold += g;
        q -= lb->first;
        lb->second.pop();

        if (lb->second.empty()) {
            m.erase(lb);
        }
    }
}
    }
    
    return 0;
}