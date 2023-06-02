#include <iostream>
#include <string>
using namespace std;

string alphabet{"ABCDEFGHIJKLMNOPQRSTUVWXYZ"};
char decode{'?'};
void encrypt(string cipher, string key);
void decrypt(string cipher, string key);

int main(){
    string cipher;
    string key;
    cin >> cipher >> key;
    //encrypt(cipher, key);
    decrypt(cipher, key);

    return 0;
}

void encrypt(string cipher, string key){
    string mutateMsg;
    mutateMsg = cipher;
    mutateMsg.insert(0, key);
    mutateMsg.erase(mutateMsg.length() - key.length());
    for (size_t i = 0; i < size(mutateMsg); i++){
        int append = alphabet.find(mutateMsg[i]) + alphabet.find(cipher[i]);
        if(append > 25) append -= 26;
        cipher[i] = alphabet[append];
    }
    cout << cipher << '\n';
}

void decrypt(string cipher, string key){
    string mutateMsg{""};
    string unknown{""};
    for (size_t i = 0; i < cipher.length(); i++){
        mutateMsg += decode;
        unknown += decode;
    }
    mutateMsg.insert(0, key);
    mutateMsg.erase(mutateMsg.length() - key.length());
    for (size_t i = 0; i < cipher.length(); i++){
        int append = alphabet.find(cipher[i]) - alphabet.find(mutateMsg[i]);
        if(append < 0) append += 26;
        unknown[i] = alphabet[append];
        int temp = key.length() + i;
        if(temp < cipher.length()){
        mutateMsg[temp] = alphabet[append];
        }
    }
    cout << unknown <<'\n';
}
