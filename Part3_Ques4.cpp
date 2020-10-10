#include<bits/stdc++.h>
    using namespace std;
    # define ll long long
    int main(){
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        int t;
        cin>>t;
        int a[1000][1000]={0},i,j,res=0,x1,x2,y1,y2;
        while(t--){
            cin>>x1>>y1>>x2>>y2;
            for(i=x1;i<x2;i++){
                for(j=y1;j<y2;j++){
                    if(a[i][j]==0){
                        a[i][j]=1;
                        res+=1;
                    }
                }
            }
        }
        cout<<res;
    }
