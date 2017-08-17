#include<iostream> 
using namespace std;
#include<vector>








int main(){
	float a,tmp,sum=1;
	int loc;
	string str = "WTL";
	for(int i=0;i<3;i++){
		cin>>a;
		tmp=a;
		loc=0;
		for(int j=1;j<3;j++){
			cin>>a;
			if(tmp<a){
				tmp=a;
				loc=j;
			}
		}
        sum*=tmp;
			cout<<str[loc]<<" ";
		
	}
    printf("%.2f",(sum*0.65-1)*2);
	
	
}

