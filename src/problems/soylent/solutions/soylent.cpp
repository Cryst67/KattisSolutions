#include <iostream>
#include <math.h>
using namespace std;

const double calories = 400;

int main(){
    int cases;
    cin >> cases;
    for (size_t i = 0; i < cases; i++){
        int a;
        cin >> a;
        cout << ceil(a/calories) << '\n';

    }
    


    return 0;
}