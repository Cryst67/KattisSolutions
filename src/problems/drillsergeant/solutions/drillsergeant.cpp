#include <bits/stdc++.h>
using namespace std;
set<int>l;
unordered_map<int,set<int>>g;
unordered_map<int,int>c;
bool gR(int x,int y){auto it=g.find(x);return it!=g.end()&&it->second.find(y)!=it->second.end();}
void uD(int n,set<int>::iterator it,int& d){d-=c[n];c[n]=0; bool f=it!=l.begin()&&gR(n,*prev(it)),b=next(it)!=l.end()&&gR(n,*next(it)); c[n]=(f&&b)?3233:(f?323:(b?32:3));d+=c[n];}
int main(){ios_base::sync_with_stdio(0);cin.tie(0);int n,m,q,f=0;cin>>n>>m;
for(int i=0,a,b;i<m;i++){cin>>a>>b;g[a].insert(b);g[b].insert(a);}cin>>q;
for(int i=0,d,z;i<q;i++){cin>>d>>z;set<int>::iterator it;
if(d==1){l.insert(z);it=l.find(z);}
else{it=l.find(z);it=next(it);l.erase(z);if(it==l.end())it=prev(it);f-=c[z];c[z]=0;}
if(l.size()==1)uD(*it,it,f);
else{set<int>::iterator p=prev(it),n=next(it);
if(it==l.begin())uD(*it,it,f),uD(*n,n,f);
else if(n==l.end())uD(*it,it,f),uD(*p,p,f);
else uD(*it,it,f),uD(*p,p,f),uD(*n,n,f);}
cout<<f<<'\n';}}