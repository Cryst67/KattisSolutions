#include <iostream>

using namespace std;

int main(){
    int rooms{};
    int teams{};
    cin >> rooms >> teams;
    int remainder = teams%rooms;
    int rm_remainder = teams - remainder;
    int avg_size = rm_remainder/ rooms;
    int rm_counter = remainder;
    for(size_t i = 0; i < rooms; i++){
        if(rm_counter!= 0){
            for(size_t i = 0; i < avg_size; i++) cout << '*';
            cout << '*';
            rm_counter --;
        }else{
            for(size_t i = 0; i < avg_size; i++) cout << '*';
        }
        cout << '\n';
    } 
    return 0;
}