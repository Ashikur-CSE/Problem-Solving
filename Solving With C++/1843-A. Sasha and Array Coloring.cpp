#include<bits/stdc++.h>
using namespace std;
int main(){
    int t;
    cin>>t;
    for (int k=0;k<t;k++){
    int n,sum=0;
    cin>>n;
    int arr[n];
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }
    sort(arr,arr+n);
    for(int j=0;j<n/2;j++){
        sum+=(arr[n-j-1]-arr[j]);
    }
    cout<<sum<<endl;
    }
    return 0;
}