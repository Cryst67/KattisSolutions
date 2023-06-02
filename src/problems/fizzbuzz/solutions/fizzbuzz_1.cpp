#include <iostream>
using namespace std;

int a;
int b;
int c;

int main(){

    cin >> a;
    cin >> b;
    cin >> c;
    int count{1};
    while(count <= c){
       if(count % a ==0 && count %b ==0) cout << "FizzBuzz" <<endl;
       else if(count % a == 0) cout << "Fizz" << endl;
       else if(count % b == 0) cout << "Buzz" << endl;
    else cout << count << endl;
        count++;
    }


    return 0;
}