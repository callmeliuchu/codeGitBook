#include<iostream>
#include<vector>
using namespace std;

int main(){
	vector<float>v1(1001);
	vector<float>v2(1001);
	int k;
	int a;
	float b;
	cin>>k;
	for(int i=0;i<k;i++){
		cin>>a>>b;
		v1[a]=b;
	}
	cin>>k;
	for(int i=0;i<k;i++){
		cin>>a>>b;
		v2[a]=b;
	}
	int count=0;
	for(int i=1000;i>=0;i--){
		float c = v1[i]+v2[i];
		v1[i]=c;
		if(c!=0){
		count++;	
		}
	}
	cout<<count;
	for(int i=1000;i>=0;i--){
		if(v1[i]!=0){
			printf(" %d %.1f",i,v1[i]);
		}
	}
	
}
