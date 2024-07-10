#include<bits/stdc++.h>
#include<algorithm>
using namespace std;
int main(){
int t;
cin>>t;
while(t--){
    int k;
    cin>>k;
    int arr[k];
    for(int i=0;i<k;i++){
        cin>>arr[i];
    }

    int n= sizeof(arr)/sizeof(int);
    sort(arr,arr+n);
    arr[0]=arr[0]+1;
    int sum=1;

    for(int j=0;j<k;j++){
    sum=(sum*arr[j]);
    }
    cout<<sum<<endl;

}
}