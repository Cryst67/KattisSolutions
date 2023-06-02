#include <iostream>
using namespace std;

auto main() -> int {
    int r, c; cin >> r >> c;
    if ((r * c) % 2 == 0) cout << "Alf\n";
    else cout << "Beata\n";
}
