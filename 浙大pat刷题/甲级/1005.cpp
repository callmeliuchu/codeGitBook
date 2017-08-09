#include<iostream>
#include<vector>
using namespace std;


int main(){
	string convert[]= {"zero","one","two","three","four","five","six","seven","eight","nine"};
	string s;
	cin>>s;
	int sum=0;
	for(int i=0;i<s.length();i++){
		sum+=(s[i]-'0');
	}
	vector<int>res;
	do{
		res.push_back(sum%10);
		sum=sum/10;
	}while(sum>0);
	for(int i=res.size()-1;i>=-0;i--){
		if(i==0){
			cout<<convert[res[i]];
		}else{
			cout<<convert[res[i]]<<" ";
		}
	}
    
}
