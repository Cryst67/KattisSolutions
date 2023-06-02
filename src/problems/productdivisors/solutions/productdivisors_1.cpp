#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

const int MAX_N = 1000000;
const long long MOD = 1e9 + 7;

vector<int> sieve() {
    vector<int> prime(MAX_N + 1, 0);
    prime[0] = prime[1] = 1;

    for (int i = 2; i * i <= MAX_N; i++) {
        if (prime[i] == 0) {
            for (int j = i * i; j <= MAX_N; j += i) {
                prime[j] = 1;
            }
        }
    }
    return prime;
}

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL);

    int n;
    cin >> n;

    vector<int> prime = sieve();
    unordered_map<int, int> prime_factors;

    for (int i = 0; i < n; i++) {
        int num;
        cin >> num;

        for (int j = 2; j * j <= num; j++) {
            if (prime[j] == 0) {
                while (num % j == 0) {
                    prime_factors[j]++;
                    num /= j;
                }
            }
        }
        if (num > 1) {
            prime_factors[num]++;
        }
    }

    long long res = 1;
    for (const auto& pf : prime_factors) {
        res = (res * (pf.second + 1)) % MOD;
    }
    cout << res << endl;

    return 0;
}
