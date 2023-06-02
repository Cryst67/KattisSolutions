#include <iostream>
#include <math.h>
using namespace std;

int main(){

    int n, x, y;
    cin >> n >> x >> y;
    int arr[n];
    for (size_t i = 0; i < n; i++){
        cin >> arr[i];
        int temp = y * arr[i];
        cout << temp/x << '\n';
    }
    
    return 0;
}