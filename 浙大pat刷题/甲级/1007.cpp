#include<iostream>
#include<vector>
using namespace std;

int main(){
	int n,num;
	cin>>n;
    vector<int>vec;
    for(int i=0;i<n;i++){
    	cin>>num;
    	vec.push_back(num);
    }
    int maxsum=vec[0];
    int tmp1=0,tmp2=0;
    for(int i=0;i<n;i++){
    	int sum=0;
    	for(int j=i;j<n;j++){
    		sum=sum+vec[j];
    		if(maxsum<sum){
    		maxsum=sum;
                tmp1=i;
    		tmp2=j;
          	}

       }  
   }
           if(maxsum<0){
           cout<<0<<" "<<vec[0]<<" "<<vec[n-1];
           return 0;
           }
	cout<<maxsum<<" "<<vec[tmp1]<<" "<<vec[tmp2];
}
