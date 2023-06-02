#include <iostream>
#include <math.h>
#include <vector>
#include <algorithm>
#include <set>
using namespace std;

void primeFactors(set<long long int>& primeFac, long long int n);
void divisors(set<long long int>& divisors, set<long long int>& primeFac, long long int n);
int main(){
    long long int n; cin>> n;
    set<long long int> primeFac;
    primeFactors(primeFac, n);
    set<long long int> divisor;
    divisors(divisor, primeFac, n);
    for(auto i : divisor)cout << i << '\n';
    
    return 0;
}


void primeFactors(set<long long int>& primeFac, long long int n){
    for(long long int i = 1; i <= sqrt(n); i++){
        if(n%i == 0)primeFac.insert(i);
    }
}

void divisors(set<long long int>& divisors, set<long long int>& primeFac, long long int n){
    for(auto i : primeFac){
        divisors.insert(i);
        long long int n1 = n/i;
        divisors.insert(n1);
    }
}