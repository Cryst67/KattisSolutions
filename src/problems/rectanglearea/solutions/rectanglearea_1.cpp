#include <iostream>
#include <math.h>
using namespace std;
double distance(double x1, double y1, double x2, double y2);
int main(){
    double x1, y1, x2, y2;
    cin >> x1 >> y1 >> x2 >> y2;
    cout << distance(x1,y1,x2,y1)*distance(x1,y1,x1,y2) << '\n';

    return 0;
}

double distance(double x1, double y1, double x2, double y2)
{
    return sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2) * 1.0);
}