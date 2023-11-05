#include<iostream>
#include<cmath>
using namespace std;

int main(){
    int t;
    cin>>t;
for (int i=0;i<t;i++){
    int a,b,c;
    cin>>a>>b>>c;
    float x=abs(a-b);
    float res = (x/c)/2;
    cout<<ceil(res)<<endl;
}
return 0;
}