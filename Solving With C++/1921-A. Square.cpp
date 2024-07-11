#include<bits/stdc++.h>
#include<cmath>
using namespace std;
int main(){
    int t;
    cin>>t;
    while(t--){
        int n;
        int x[4],y[4];
        for(int i=0;i<4;i++){
            cin>>x[i]>>y[i];
        }
        sort(x,x+4);
        int area = (x[2]-x[1])*(x[2]-x[1]);
        cout<<area<<endl;
        
                }
        
    }

