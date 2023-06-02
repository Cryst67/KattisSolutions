#include <iostream>
#include <string>
using namespace std;

const char b{'B'};
const char w{'W'};
int main(){
    string input;
    cin >> input;
    int b_counter = 0;
    int w_counter = 0;
    string balance;
    for (size_t i = 0; i < size(input); i++){
        if(input[i] == b) b_counter++;
        else if(input[i] == w) w_counter++;
        
    }

    if(b_counter == w_counter) cout << 1 <<'\n';
    else cout << 0 <<'\n';
    return 0;
}