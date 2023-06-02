#include <iostream>

using namespace std;

bool add(int i, int j, int k);
int main(){

    int stars = 0;
    cin >> stars;
    cout << stars << ":\n"; 
    int x;
    if(stars % 2 ==0) x = stars;
    else x = stars + 1;
    for (size_t i = 2; i <= x/2; i++){
        for (size_t j = 1; j < i+1; j++){
            if((i - j) <= 1){
                if(add(i,j,stars)) cout << i << ',' << j << '\n';
            }
        }
        
    }
    return 0;
}

bool add(int i, int j, int k){
    int sum = 0;
    while(true){
        if(!((sum + i) > k)){
            sum = sum + i; 
        }
        else break;
        if(!((sum + j) > k)){
            sum = sum + j;
        }
        else break;
    }
    if(sum == k) return true;
    else return false;
}