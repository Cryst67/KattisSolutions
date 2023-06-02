#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

auto main() -> int {
    int n, m; cin >> n >> m;
    unordered_map<int, vector<int>> graph;
    for (int i = 0; i < m; i++){
        int a, b; cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }
    for(int i = 0; i < n; i++){
        int succ_factor = i + 1;
        int pop_factor = graph[i + 1].size();
        cout << pop_factor - succ_factor << ' ';
    }
    cout << '\n';
}
