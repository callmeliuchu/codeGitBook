#include<iostream>
using namespace std;


int main(){
	 int n;
	 cin>>n;
	 int s=0;
	 int sum=n*5;
	 int next;
	 for(int i=0;i<n;i++){
        cin>>next;
        if(next>s){
         sum=sum+(next-s)*6;
        }else if(next<s){
         sum=sum+(s-next)*4;
        }
        s=next;
	 }
	 cout<<sum;
}