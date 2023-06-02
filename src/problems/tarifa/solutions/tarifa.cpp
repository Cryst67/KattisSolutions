#include <iostream>
using namespace std;

int main(){
    int mBytes;
    int months;
    int tempBytes;

    cin >> mBytes >> months;

    int totalBytes = mBytes;

    for (size_t i = 0; i < months; i++)
    {
        cin >> tempBytes;
        totalBytes -= tempBytes;
        totalBytes += mBytes;
    }
    
    cout << totalBytes << endl;


    return 0;
}