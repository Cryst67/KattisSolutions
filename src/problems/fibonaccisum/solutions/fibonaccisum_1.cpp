#include <iostream>
#include <vector>
using namespace std;int m[50]={0};int r(vector<int>& s,int& n,int j){for(int i=0;i<j;i++){int cur=m[i];int prev;if(i>0)prev=m[i-1];if(n-m[i]<0){n-=m[i-1];j=i-1;s.push_back(m[i-1]);break;}}return j;}int f( int n){if(m[n]!=0)return m[n];if(n < 2)return 1;m[n-1]=f(n-1);m[n-2]=f(n-2);return m[n-1]+m[n-2];}
int main(){f(49);int n;cin>>n;vector<int>s;int j=50;while(n!=0){j=r(s,n,j);}for(int i=s.size()-1;i>-1;i--){cout<<s[i]<<' ';}cout<<'\n';}