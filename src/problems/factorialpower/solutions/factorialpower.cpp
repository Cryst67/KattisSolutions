#include <iostream>
#include <map>

using namespace std;

typedef long long ll;

map<ll, int> prime_factors(ll n) {
    map<ll, int> factors;

    for (ll j = 2; j * j <= n; j++) {
        while (n % j == 0) {
            factors[j]++;
            n /= j;
        }
    }

    if (n > 1) {
        factors[n]++;
    }

    return factors;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    ll n, m;
    cin >> n >> m;

    map<ll, int> factors_n = prime_factors(n);

    ll min_k = 1e18;
    for (const auto &factor : factors_n) {
        ll p = factor.first;
        int count = factor.second;

        ll cnt = 0;
        for (ll i = p; i <= m; i *= p) {
            cnt += m / i;
        }

        min_k = min(min_k, cnt / count);
    }

    cout << min_k << endl;

    return 0;
}
