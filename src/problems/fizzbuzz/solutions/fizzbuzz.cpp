#include <iostream>
using namespace std;

int a;
int b;
int c;

int main(){

    cin >> a >> b >> c;
    for(int i = 1; i <=c; i++){
       if(i % a ==0 && i %b ==0) cout << "FizzBuzz" <<endl;
       else if(i % a == 0) cout << "Fizz" << endl;
       else if(i % b == 0) cout << "Buzz" << endl;
        else cout << i << endl;
    }
    return 0;
}