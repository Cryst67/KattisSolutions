#include <iostream>
#include <vector>
#include <stack>
#include <unordered_map>
using namespace std;

void dfs(int &, int &, vector<int> &, vector<bool> &, vector<bool> &, unordered_map<int, vector<int>> &, unordered_map<int, bool> &);

int main()
{
    int n, b, m;
    cin >> n >> b >> m;
    vector<int> components(n + 1);
    vector<bool> boats(n + 1);
    vector<bool> visited(n + 1);
    unordered_map<int, vector<int>> graph;
    unordered_map<int, bool> boatOrNot;
    for (size_t i = 0; i < b; i++)
    {
        int boat;
        cin >> boat;
        boats[boat] = 1;
    }

    for (size_t i = 0; i < m; i++)
    {
        int a, b;
        cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }
    int count = 1;
    for (int i = 1; i <= n; i++)
    {
        if (!visited[i])
        {
            dfs(i, count, components, visited, boats, graph, boatOrNot);
            count++;
        }
    }
    count--;
    for (auto &[key, val] : boatOrNot)
    {
        if (val == 1)
            count--;
    }
    cout << count << '\n';
    return 0;
}

void dfs(int &node, int &count, vector<int> &components, vector<bool> &visited, vector<bool> &boats, unordered_map<int, vector<int>> &graph, unordered_map<int, bool> &boatOrNot)
{
    stack<int> s;
    s.push(node);
    while (!s.empty())
    {
        int currentNode = s.top();
        s.pop();
        if (graph.count(currentNode) == 0)
        {
            if (boatOrNot.count(count) == 0)
            {
                boatOrNot[count] = boats[currentNode];
            }
            else if (boatOrNot[count] == 0)
            {
                boatOrNot[count] = boats[currentNode];
            }

            visited[currentNode] = 1;
            components[currentNode] = count;
            break;
        }
        visited[currentNode] = 1;
        components[currentNode] = count;
        if (boatOrNot.count(count) == 0)
        {
            boatOrNot[count] = boats[currentNode];
        }
        else if (boatOrNot[count] == 0)
        {
            boatOrNot[count] = boats[currentNode];
        }
        for (auto &nbr : graph[currentNode])
        {
            if (!visited[nbr])
                s.push(nbr);
        }
    }
}