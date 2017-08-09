#include<iostream> 
#include<vector>
using namespace std;


int main(){
	int a;
	int b;
	cin>>a>>b;
	int c=a+b;
	if(c<0){
		cout<<"-";
		c=-c;
	}
	vector<int>res;
    do{
    	res.push_back(c%10);
    	c=c/10;
    }while(c!=0);
    for(int i=res.size()-1;i>=0;i--){
    	cout<<res[i];
    	if(i%3==0 && i!=0){
    		cout<<",";
    	}
    }
}
