#include <iostream>
#include <string>
using namespace std;

string w{"WWW"};
string b{"BBB"};

void resetCounter(int& a, int& b);
int main(){

    int n;
    cin >> n;
    char arr[n][n];
    int b_counter = 0;
    int w_counter = 0;
    size_t count = 0;
    bool correct = true;

    for (size_t i = 0; i < n; i++){
        for (size_t j = 0; j < n; j++){
            char temp; 
            cin >> temp;
            arr[i][j] = temp;
        }
    }
    for (size_t i = 0; i < n; i++){
        string check{""};
        for (size_t j = 0; j < n; j++){
            if(arr[i][j] == 'W'){
                w_counter++;
            }
            else if(arr[i][j] == 'B'){
                b_counter++;
            }
            check += arr[j][i];
        }
        if(check.find(w) != string::npos ||check.find(b) != string::npos ){
            correct = false;
            goto pResult;
        }
        if(w_counter != b_counter) {
            correct = false;
            goto pResult;
        }
    }

    resetCounter(b_counter,w_counter);

    if(correct){
        for (size_t i = 0; i < n; i++){
            string check {""};
            for (size_t j = 0; j < n; j++){
                if(arr[j][i] == 'W'){
                    w_counter++;
                }
                else if(arr[j][i] == 'B'){
                    b_counter++;
                }
                check += arr[i][j];
            }
            if(check.find(w) != string::npos || check.find(b) != string::npos ){
            correct = false;
            goto pResult;
            }
            if(w_counter != b_counter) {
                correct = false;
                goto pResult;
            }
    }

    pResult: cout << ((correct)? 1 : 0 ) << '\n';

    return 0;
}

}

void resetCounter(int& a, int& b){
    a = 0;
    b = 0;
}