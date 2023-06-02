#include <set>
#include <vector>
#include <utility>
#include <iterator>
#include <iostream>
#include <unordered_map>
using namespace std;

set<int>l;
unordered_map<int,set<int>>g;
unordered_map<int,int>c;

bool gR(int x,int y){
    auto it = g.find(x);
    return it != g.end() && it->second.find(y) != it->second.end();
}

void uD(int n, set<int>::iterator it, int& d){
    if(c.find(n) == c.end()) c[n] = 0;
    d-= c[n];
    c[n] = 0;
    bool front_rel = 0;
    bool back_rel = 0;
    if(it != l.begin()) front_rel = gR(n, *prev(it));
    if(next(it) != l.end()) back_rel = gR(n, *next(it));
    if(front_rel && back_rel) c[n] += 3233;
    else if(front_rel) c[n] += 323;
    else if(back_rel) c[n] += 32;
    else c[n] += 3;
    d += c[n];
}

int main() {
    int n, m; cin >> n >> m;
    for (size_t i = 0; i < m; i++) {
        int a, b; cin >> a >> b;
        g[a].insert(b);
        g[b].insert(a);
    }
    int q; cin >> q;
    int discontent = 0;
    for (size_t i = 0; i < q; i++) {
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
            discontent -= c[z];
            c[z] = 0;
        }
        if(l.size() == 1){
            uD(*it, it, discontent);
        }
        else if(it == l.begin()){
            uD(*it, it, discontent);
            uD(*next(it), next(it), discontent);
        }
        else if(next(it) == l.end()){
            uD(*it, it, discontent);
            uD(*prev(it), prev(it), discontent);
        }
        else{
            uD(*it, it, discontent);
            uD(*prev(it), prev(it), discontent);
            uD(*next(it), next(it), discontent);
        }
        cout << discontent << '\n';
    }
    return 0;
}
