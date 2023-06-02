#include <iostream>
using namespace std;

auto main() -> int
{
    long long int A, B; cin >> A >> B;
    if (A % B == 0)
    {
        cout << 0 << '\n';
        exit(0);
    }
    if (A < B)
    {
        if(A <= (B/2)){
            cout << A << '\n';
        }
        else cout << B - A << '\n';
        exit(0);
    }
    long long int p = A / B;
    long long int q = p + 1;
    cout << min(abs((p * B) - A), abs((q * B) - A)) << '\n';
}