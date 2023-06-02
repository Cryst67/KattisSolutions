#include <iostream>
using namespace std;

int main(){
 
    int t, s, n;
    cin >> t >> s >> n;
    int arr[n+1];
    for(int i = 1; i <=n; i++){
        cin >> arr[i];
    }
    int ind = 1;
    int top = 0, bottom = s;
    for (size_t i = 0; i <= t; i++){
        if(top != 0){
            top --;
            bottom ++;
        }
        if(i == arr[ind]){
            ind ++;
            int temp = bottom;
            bottom = top;
            top = temp;
        }
    }
    cout << top << '\n';
    return 0;
}