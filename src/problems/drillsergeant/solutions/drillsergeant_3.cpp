#include <set>
#include <iterator>
#include <iostream>
#include <unordered_map>
using namespace std;

set<int>l;
unordered_map<int,set<int>>g;
unordered_map<int,int>c;

bool gR(const int& x,const int& y){
    auto it = g.find(x);
    return it != g.end() && it->second.find(y) != it->second.end();
}

void uD(const int& n, const set<int>::iterator& it, int& d){
    d-= c[n];
    c[n] = 0;
    bool f = 0, b = 0;
    if(it != l.begin()) f = gR(n, *prev(it));
    if(next(it) != l.end()) b = gR(n, *next(it));
    if(f && b) c[n] += 3233;
    else if(f) c[n] += 323;
    else if(b) c[n] += 32;
    else c[n] += 3;
    d += c[n];
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n, m; cin >> n >> m;
    for (int i = 0; i < m; i++) {
        int a, b; cin >> a >> b;
        g[a].insert(b);
        g[b].insert(a);
    }
    int q; cin >> q;
    int f = 0;
    for (int i = 0; i < q; i++) {
        int d, z; cin >> d >> z;
        set<int>::iterator it;
        if (d == 1) {
            l.insert(z);
            it = l.find(z);
        } else {
            it = l.find(z);
            it = next(it);
            l.erase(z);
            if(it == l.end()) it = prev(it);
            f -= c[z];
            c[z] = 0;
        }
        if(l.size() == 1) uD(*it, it, f);
        else if(it == l.begin()){ uD(*it, it, f); uD(*next(it), next(it), f);}
        else if(next(it) == l.end()){ uD(*it, it, f); uD(*prev(it), prev(it), f);}
        else{ uD(*it, it, f); uD(*prev(it), prev(it), f); uD(*next(it), next(it), f);}
        cout << f << '\n';
    }
}