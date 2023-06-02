#include <iostream>
#include <string>
using namespace std;

string key{"ABCDEFGHIJKLMNOPQRSTUVWXYZ_."};

void reverseStr(string& str);
void shiftStr(string& key, string& str, int shift);
int main(){

    while(true){
        int n; cin >> n;
        if(n == 0) break;
        string str; cin >> str;
        reverseStr(str);
        shiftStr(key, str, n);
        cout << str << '\n';
    }
    return 0;
}

void reverseStr(string& str){
    int n = str.length();
    for (int i = 0; i < n / 2; i++)
        swap(str[i], str[n - i - 1]);
}

void shiftStr(string& key, string& str, int shift){
    for(int i = 0; i < str.length(); i++){
        int index = key.find(str[i]);
        int new_index =  index + shift;
        if(new_index > 27) new_index-=28;
        str[i] = key[new_index];
    }
}