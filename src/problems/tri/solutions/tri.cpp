#include <iostream>

using namespace std;

int main(){
   int result{};
   int result1{};
   int nresult{};
   cin >> result >> nresult >> result1;
   if(result == nresult + result1) cout << result <<'=' << nresult << "+" << result1 << '\n';
   else if(result + nresult == result1) cout << result <<'+' << nresult << "=" << result1 << '\n';
   else if(result == nresult - result1) cout << result <<'=' << nresult << "-" << result1 << '\n';
   else if(result - nresult == result1) cout << result <<'-' << nresult << "=" << result1 << '\n';
   else if(result == nresult * result1) cout << result <<'=' << nresult << "*" << result1 << '\n';
   else if(result * nresult == result1) cout << result <<'*' << nresult << "=" << result1 << '\n';
   else if(result == nresult / result1) cout << result <<'=' << nresult << "/" << result1 << '\n';
   else if(result / nresult == result1) cout << result <<'/' << nresult << "=" << result1 << '\n';
    return 0;
}