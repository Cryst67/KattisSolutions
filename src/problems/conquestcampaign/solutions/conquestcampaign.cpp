#include <iostream>
#include <queue>
#include <utility>
using namespace std;

int main(int argc, char const *argv[])
{
    queue <pair<int,int>> q;
    int r, c, n; cin >> r >> c >> n;
    int rows = r + 1, cols = c + 1;
    bool visited[rows][cols];

    for (size_t i = 0; i < rows; i++)
    {
        for (size_t j = 0; j < cols; j++)
        {
            visited[i][j] = 0;
        }    
    }
    

    for (size_t i = 0; i < n; i++)
    {
        int x, y; cin >> x >> y;
        visited[x][y] = 1;
        q.push(make_pair(x,y));
    }

    int day = 0;

    while(!q.empty())
    {
        int count = q.size();
        for (size_t i = 0; i < count; i++)
        {
            pair<int,int> here = q.front();
            q.pop();
            int top = here.first + 1;
            int bottom = here.first - 1;
            int left = here.second - 1;
            int right = here.second + 1;
            if((top >= 1 && top < rows) 
            && (here.second >= 1 && here.second < cols)
            && (!visited[top][here.second]))
            {
                visited[top][here.second] = 1;
                q.push(make_pair(top, here.second));
            }
            if((bottom >= 1 && bottom < rows) 
            && (here.second >= 1 && here.second < cols)
            && (!visited[bottom][here.second]))
            {
                visited[bottom][here.second] = 1;
                q.push(make_pair(bottom, here.second));
            }
            if((here.first >= 1 && here.first < rows) 
            && (left >= 1 && left < cols)
            && (!visited[here.first][left]))
            {
                visited[here.first][left] = 1;
                q.push(make_pair(here.first, left));
            }
            if((here.first >= 1 && here.first < rows) 
            && (right >= 1 && right < cols)
            && (!visited[here.first][right]))
            {
                visited[here.first][right] = 1;
                q.push(make_pair(here.first, right));
            }
        }
        day++;
    }
    
    cout << day << '\n';

    return 0;
}