#include <iostream>
using namespace std;

int main(){
    int a;
    int b;
    cin >> a >> b;
    while(a +(b*b)!= 0){
        if(a + b == 13){
            cout << "Never speak again." << endl;
        }else if(a > b){
            cout << "To the convention." << endl;
        }else if(a < b){
            cout << "Left beehind." << endl;
        }else if(a == b){
            cout << "Undecided." << endl;
        }
    cin >> a >> b;
    }

    return 0;
}