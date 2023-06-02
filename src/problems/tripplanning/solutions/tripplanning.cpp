#include <vector>
#include <utility>
#include <iostream>
#include <unordered_map>
using namespace std;

auto main() -> int
{
    int N, M;
    cin >> N >> M;
    unordered_map<int, vector<pair<int, int>>> graph;
    for (size_t i = 0; i < M; i++)
    {
        int a, b;
        cin >> a >> b;
        graph[a].push_back({b, i + 1});
        graph[b].push_back({a, i + 1});
    }
    int curCity = 1;
    vector<int> order;
    while (curCity != N)
    {
        int check = curCity;
        for (auto p : graph[curCity])
        {
            if (p.first == curCity + 1)
            {
                curCity += 1;
                order.push_back(p.second);
                break;
            }
        }
        if (check == curCity)
        {
            cout << "impossible\n";
            exit(0);
        }
    }
    bool flag = false;
    for (auto p : graph[curCity])
    {
        if (p.first == 1)
        {
            flag = true;
            order.push_back(p.second);
            break;
        }
    }
    if (!flag)
    {
        cout << "impossible\n";
        exit(0);
    }
    for (auto i : order)
    {
        cout << i << '\n';
    }
}