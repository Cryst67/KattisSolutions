#include <algorithm>
#include <iostream>
#include <utility>
#include <vector>
#include <set>
using namespace std;

class UnionFind{
    public:
    vector<int> id, sz;
    UnionFind(int n){
        id.resize(n);
        sz.resize(n);
        for (size_t i = 0; i < n; i++){
            id[i] = i;
            sz[i] = 1;
        }
    }
    auto find(int p) -> int {
        int root = p;
        while (root != id[root]) root = id[root];
        while (p != root){
            int next = id[p];
            id[p] = root;
            p = next;
        }
        return root;
    }
    auto connected(int p, int q) -> bool {return find(p) == find(q);}
    auto size(int p) -> int {return sz[find(p)];}
    auto Union(int p, int q) -> void {
        int r1 = find(p);
        int r2 = find(q);
        if (r1 == r2) return;
        if (sz[r1] < sz[r2]){
            sz[r2] += sz[r1];
            id[r1] = r2;
        }else{
            sz[r1] += sz[r2];
            id[r2] = r1;
        }
    }
};

struct Edge{
    int from, to, cost;
    Edge(int f, int t, int c){
        from = f;
        to = t;
        cost = c;
    }
};

auto manhattanDistance(int x, int y, int x1, int y1) -> int {
    return abs(x - x1) + abs(y - y1);
}

auto main() -> int {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    int n; cin >> n;
    vector<pair<int,int>> v(n);
    for (size_t i = 0; i < n; i++) {
        int a, b; cin >> a >> b;
        v[i] = {a, b};
    }
    vector<Edge> edges;
    edges.reserve(n*(n-1)/2);
    for (size_t i = 0; i < n; i++) {
        int x = v[i].first, y = v[i].second;
        for (size_t j = i + 1; j < n; j++) {
            int x1 = v[j].first, y1 = v[j].second;
            edges.emplace_back(Edge(i, j, manhattanDistance(x, y, x1, y1)));
        }
    }
    sort(edges.begin(), edges.end(), [](const Edge& a, const Edge& b){
        return a.cost < b.cost;
    });

    int time = 0;
    UnionFind uf = UnionFind(n);
    for(auto& edge : edges){
        int p = edge.from, q = edge.to;
        if(uf.connected(p, q)) continue;
        uf.Union(p, q);
        time += edge.cost;
        if(uf.size(0) == n) break;
    }
    cout << time * 2 << '\n';
    return 0;
}