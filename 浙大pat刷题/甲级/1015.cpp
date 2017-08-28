#include<iostream>
#include<math.h>
using namespace std;

int isPrime(int n){
	if(n==1){
		return 0;
	}
	for(int i=2;i<=sqrt(n);i++){
		if(n%i==0){
			return 0;
		}
	}
	return 1;
}

int  reverse(int n,int d){
	int sum=0;
	while(n>0){
		int r = n%d;
		sum = sum*d + r;
		n = n/d;
	}
	return sum;
}

int isTrue(int n,int d){
//	cout<<n<<" "<<reverse(n,d)<<endl;
//	cout<<isPrime(n)<<" "<<isPrime(reverse(n,d)); 
	return isPrime(n) && isPrime(reverse(n,d));
}


int main(){
	int a,b;
	do{
		cin>>a;
		if(a<0){
			return 0;
		}
		cin>>b;
//		cout<<a<<" "<<b<<endl;	
        if(isTrue(a,b)){
        	cout<<"Yes"<<endl;
        }else{
        	cout<<"No"<<endl;
        }
	}while(true);
	
}
