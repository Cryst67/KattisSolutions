#include <iostream>
#include <algorithm>
using namespace std;

int main(int argc, char const *argv[]){

    int n; cin >> n;
    int arr[3][n];
    for (size_t i = 0; i < 3; i++)
    {
        for (size_t j = 0; j < n; j++)
        {
            int temp; cin >> temp;
            arr[i][j] = temp;
        }
    }

    for (size_t i = 0; i < n; i++){
        int* temp = new int[3];
        int count = 0;
        for (size_t j = 0; j < 3; j++){
            temp[count] = arr[j][i];
            count++;
        }
        sort(temp, temp+3);
        cout << temp[1] << ' ';
        delete[] temp;
    }
        cout << '\n';

    return 0;
}