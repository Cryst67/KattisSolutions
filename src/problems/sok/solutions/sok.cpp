#include <iostream>
using namespace std;

double min(double a, double b, double c);

int main(){

  double a, b, c;
  double i, j, k;
  cin >> a >> b >> c >> i >> j >> k;
  double r_a = a/i;
  double r_b = b/j;
  double r_c = c/k;
  double minVal = min(r_a,r_b,r_c);
  double rm_a = a - (i * minVal);
  double rm_b = b - (j * minVal);
  double rm_c = c - (k * minVal);
  cout << fixed;
  cout.precision(6);
  cout << rm_a << ' ';
  cout << rm_b << ' ';
  cout << rm_c << '\n';

  return 0;
}

double min(double a, double b, double c){
  double arr[]{a, b, c};
  double min = arr[0];
  for (size_t i = 1; i < size(arr); i++){
    if(arr[i] < min) min = arr[i];
  }
  return min;
}