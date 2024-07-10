#include<bits/stdc++.h>
#include<algorithm>
using namespace std;
int main(){
    int t;
    cin>>t;
while(t--){
        string text;
        cin>>text;

        char char1='A';
        char char2='B';

        int countA=0;
        int countB=0;

       for (int i=0;i<text.length();i++){
        if(text[i]==char1){
            countA+=1;
       }
       else{
        countB+=1;
       }
    }

   if(countA>countB){
    cout<<"A"<<endl;
}
else{
    cout<<"B"<<endl;
}
}
}


    

