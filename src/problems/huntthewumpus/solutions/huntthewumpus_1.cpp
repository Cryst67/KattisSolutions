#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <limits>
#include <set>
using namespace std;

int generateLocation(int seed);
int getManhattanDistance(set<string> &, string);

int main()
{
    int seed;
    cin >> seed;
    set<string> coordinates;
    while (coordinates.size() < 4)
    {
        seed = generateLocation(seed);
        string location = to_string(seed);
        location = location.substr(location.size() - 2, 2);
        coordinates.insert(location);
    }
    string in;
    set<string>::iterator it;
    int score = 0;
    int i = 0;
    while (!coordinates.empty())
    {
        cin >> in;
        it = find(coordinates.begin(), coordinates.end(), in);
        if (it != coordinates.end())
        {
            cout << "You hit a wumpus!\n";
            coordinates.erase(it);
        }
        if (!coordinates.empty())
        {
            cout << getManhattanDistance(coordinates, in) << '\n';
        }
            score++;
    }
    cout << "Your score is " << score << " moves.\n";
}

int generateLocation(int seed)
{
    return seed + (seed / 13) + 15;
}

int getManhattanDistance(set<string> &coordinates, string s)
{
    int manhattanDistance = numeric_limits<int>::max();
    for (auto coordinate : coordinates)
    {
        int x1 = stoi(string(1, coordinate[0]));
        int y1 = stoi(string(1, coordinate[1]));
        int x2 = stoi(string(1, s[0]));
        int y2 = stoi(string(1, s[1]));
        int distance = abs(x1 - x2) + abs(y1 - y2);
        if (distance < manhattanDistance)
        {
            manhattanDistance = distance;
        }
    }
    return manhattanDistance;
}