#include <bits/stdc++.h>

using namespace std;

map<string, int> mapping = {
        {"**** ** ** ****", 0},
        {"  *  *  *  *  *", 1},
        {"***  *****  ***", 2},
        {"***  ****  ****", 3},
        {"* ** ****  *  *", 4},
        {"****  ***  ****", 5},
        {"****  **** ****", 6},
        {"***  *  *  *  *", 7},
        {"**** ***** ****", 8},
        {"**** ****  ****", 9}};

int main(){
    string line;
    vector<string> nums(8, "");
    int chars;
    for(int i = 0; i < 5; i++){
        getline(cin, line);
        chars = line.size() / 4 + 1;
        for(int j = 0; j < chars; j++){
            nums[j] += line.substr(j * 4, 3);
        }
    }
    int time = 0;
    bool valid = true;
    for(int i = 0; i < chars; i++){
        auto mapptr = mapping.find(nums[i]);
        if(mapptr == mapping.end()){
            valid = false;
            break;
        } else {
            time *= 10;
            time += (*mapptr).second;
        }
    }
    if(valid && time % 6 == 0){
        cout << "BEER!!";
    } else {
        cout << "BOOM!!";
    }
    return 0;
}