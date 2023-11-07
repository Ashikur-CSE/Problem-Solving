#include<bits/stdc++.h>
using namespace std;

int main(){
    int t,n;
    cin >>t;
    while(t--){
          string s;
    cin>>n>>s;
    char ch = s[0];
    for(int i=1;i<n;i++){
        if (ch==s[i]){
            cout<<ch;
            ch=s[i+1];
            i++;
        }
        else{
            continue;
        }


    }
    cout<<endl;

    }
  
return 0;
}

