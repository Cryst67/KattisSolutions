#include <iostream>
#include <string>
using namespace std;

int main(int argc, char const *argv[]){

    int n; cin >> n;
    string s; cin >>  s;
    int coffee = 0;
    int awake = 0;
    for (size_t i = 0; i < n; i++){
        if(s[i] == '1'){
            awake++;
            if(coffee == 0) coffee+=2;
            else if(coffee == 1) coffee++;
        }else{
            if(coffee > 0){
                awake++;
                coffee--;
            }
        }
    }
    
    cout << awake << '\n';
    
    
    return 0;
}