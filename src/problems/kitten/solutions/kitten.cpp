#include <bits/stdc++.h>
using namespace std;

int main(){
    // #ifndef TESTING
    // freopen("input.txt", "r", stdin);
    // freopen("output.txt", "w", stdout);
    // #endif 

    map<string, string> parents;
    string line;
    getline(cin, line);
    string curr_branch = line.substr(0, line.size());
    
    while(getline(cin, line)){
        stringstream linestream(line);
        string token;
        linestream >> token;
        if(token == "-1"){
            break;
        }
        string parent = token;
        while(linestream >> token){
            parents.insert({token, parent});
        }
    }

    cout << curr_branch << " ";
    auto it = parents.find(curr_branch);
    while(it != parents.end()){
        curr_branch = (*it).second;
        cout << curr_branch << " ";
        it = parents.find(curr_branch);
    }
    return 0;
}