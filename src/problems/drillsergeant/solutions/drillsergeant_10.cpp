#include <set>
#include <vector>
#include <utility>
#include <iterator>
#include <iostream>
#include <algorithm>
#include <unordered_map>
using namespace std;

set<int> line;
unordered_map<int, set<int>> graph;
unordered_map<int, int> contributions;

bool getRelation(int, int);
int updateDiscontent(int n, set<int>::iterator, int& d);

auto main() -> int {
    int n, m; cin >> n >> m;
    for (size_t i = 0; i < m; i++) {
        int a, b; cin >> a >> b;
        graph[a].emplace_hint(graph[a].end(), b);
        graph[b].emplace_hint(graph[b].end(), a);
    }
    int q; cin >> q;
    int discontent = 0;
    for (size_t i = 0; i < q; i++) {
        int d, z; cin >> d >> z;
        set<int>::iterator it;
        if (d == 1) {
            line.insert(z);
            it = line.find(z);
        } else {
            it = line.find(z);
            it = next(it);
            line.erase(z);
            if(it == line.end()) it = prev(it);
            discontent -= contributions[z];
            contributions[z] = 0;
        }
        if(line.size() == 1){
            discontent = updateDiscontent(*it, it, discontent);
        }
        else if(it == line.begin()){
            discontent = updateDiscontent(*it, it, discontent);
            discontent = updateDiscontent(*next(it), next(it), discontent);
        }
        else if(next(it) == line.end()){
            discontent = updateDiscontent(*it, it, discontent);
            discontent = updateDiscontent(*prev(it), prev(it), discontent);
        }
        else{
            discontent = updateDiscontent(*it, it, discontent);
            discontent = updateDiscontent(*prev(it), prev(it), discontent);
            discontent = updateDiscontent(*next(it), next(it), discontent);
        }
        cout << discontent << '\n';
    }
    return 0;
}

int updateDiscontent(int n, set<int>::iterator it, int& d){
    if(contributions.find(n) == contributions.end()) contributions[n] = 0;
    d-= contributions[n];
    contributions[n] = 0;
    bool front_rel = 0;
    bool back_rel = 0;
    int front;
    int back;
    if(it != line.begin()){
        front = *prev(it);
        front_rel = getRelation(n, front);
    }
    if(next(it) != line.end()){
        back = *next(it);
        back_rel = getRelation(n, back);
    }
    if(front_rel && back_rel) contributions[n] += 3233;
    else if(front_rel) contributions[n] += 323;
    else if(back_rel) contributions[n] += 32;
    else contributions[n] += 3;
    d += contributions[n];
    return d;
}

bool getRelation(int x, int y){
    auto it = graph.find(x);
    if (it != graph.end() && it->second.find(y) != it->second.end()) {
        return true;
    }
    return false;
}