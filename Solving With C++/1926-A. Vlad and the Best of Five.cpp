#include<bits/stdc++.h>
using namespace std;
int main(){
    int t;
    cin>>t;
    while(t--){
        string text;
        cin>>text;
        int a,b;
        char s='A';
        char s2='B';
        for(int i;i<text.length();i++){
            if(text[i]==s){
                a=a+1; 
            }
            else if(text[i]==s2){
                b=b+1;
            }
        }
        cout<<a<<"\n";
        cout<<b;


    }
}