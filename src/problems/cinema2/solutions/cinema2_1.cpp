#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

auto main() -> int{
    int n, m; cin >> n >> m;
    vector<int> groups;
    for (size_t i = 0; i < m; i++)
    {
        int group; cin >> group;
        groups.push_back(group);
    }
    reverse(groups.begin(), groups.end());
    for (int i = m - 1; i > -1; i--)
    {
        if (n < groups[i])
            break;
        n -= groups[i];
        groups.pop_back();
    }
    cout << groups.size() << '\n';
}
