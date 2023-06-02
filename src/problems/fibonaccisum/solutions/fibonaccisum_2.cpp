#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

long long int memo[50] = {0};

auto fib(long long int) -> long long int;
auto getRemainder(vector<long long int>&, long long int &, int) -> long long int;
auto main() -> int
{
    fib(50);
    long long int n; cin >> n;
    vector<long long int> sums;
    int index = 50;
    while (n != 0)
    {
        index = getRemainder(sums, n, index);
    }
    for(int i = sums.size() - 1; i > - 1;i--){
        cout << sums[i] << ' ';
    }
    cout << '\n';
}

auto getRemainder(vector<long long int>& sums, long long int &n, int index) -> long long int
{
    for (int i = 0; i < index; i++)
    {
        long long int cur = memo[i];
        long long int prev;
        if (i > 0)
            prev = memo[i - 1];
        if (n - memo[i] < 0)
        {
            n -= memo[i - 1];
            index = i - 1;
            sums.push_back(memo[i - 1]);
            break;
        }
    }
    return index;
}

auto fib(long long int n) -> long long int
{
    if (memo[n] != 0)
        return memo[n];
    if (n < 2)
        return 1;
    memo[n - 1] = fib(n - 1);
    memo[n - 2] = fib(n - 2);
    return memo[n - 1] + memo[n - 2];
}