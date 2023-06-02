#include <iostream>

using namespace std;

int main(){
    int n, k;
    cin >> n >> k;
    int arr[n+1];
    arr[0] = -1;
    for (size_t i = 1; i < n+1; i++){
        cin >> arr[i];
    }
    for (size_t i = 1; i < n+1; i++){
        if(i%k == 0) cout << arr[i] << ' ';
    }
    cout << '\n';
    return 0;
}