#include<bits/stdc++.h>
using namespace std;
int main(){
    int t;
    cin>>t;
    for (int i=0; i<t; i++){
        int a,b,c;
        cin>>a>>b>>c;
        if (a!=b && a!=c){
            cout<<a<<"\n";
        }
        else if(b!=a && b!=c){
            cout<<b<<"\n";
        }
        else{
            cout<<c<<"\n";
        }

    }

}