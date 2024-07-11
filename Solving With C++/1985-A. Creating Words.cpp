#include<bits/stdc++.h>
using namespace std;
int main(){
    int t;
    cin>>t;
    while(t--){
        string a,b; 
        cin>>a>>b;
        string a2=a.substr(1,2);
        string b2 =b.substr(1,2);
        cout<<b[0]+a2 +" ";
        cout<<a[0]+b2<<endl;
        
           }
}