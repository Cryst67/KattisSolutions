#include <iostream>
#include <string>
using namespace std;

const char p{'P'};
const char e{'E'};
const char r{'R'};

int main(){
    int count{0};
    string input;
    cin >> input;
    for (size_t i = 0; i < size(input); i++){
        if(input[i] != p) count ++;
        if(input[i+1] != e) count ++;
        if(input[i+2] != r) count ++;
        i+=2;
    }
    cout << count << endl;
    return 0;
}