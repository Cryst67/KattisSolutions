#include <iostream>
#include <string>
using namespace std;

auto getGrade(int&, int&, int&, int&, int&, int&) -> char;

auto main() -> int {
    int a, b, c, d, e; cin >> a >> b >> c >> d >> e;
    int score; cin >> score;
    char ans = getGrade(a, b, c, d, e, score);
    cout << ans << '\n';
}

auto getGrade(int& a, int& b, int& c, int& d, int& e, int& score) -> char{
    if(score < e) return 'F';
    if(score >= e && score < d) return 'E';
    if(score >= d && score < c) return 'D';
    if(score >= c && score < b) return 'C';
    if(score >= b && score < a) return 'B';
    return 'A';
}