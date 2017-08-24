#include<iostream>
#include<vector>
using namespace std;

int change(char c){
   if(c>='0' && c<='9'){
   	return c-'0';
   }
   return c-'a'+10;
}


int num(string str,int radix){
	int sum=0;
    for(int i=0;i<str.length();i++){
    	int anum = change(str[i]);
        sum = sum*radix+anum;
    }
    return sum;
}

int minRadix(string str){
	int amin=-1;
    for(int i=0;i<str.length();i++){
       int anum = change(str[i]);
       if(amin<anum){
       	 amin=anum;
       }
    }
    return amin+1;
}








int main(){
string str1,str2;
int tag,radix;
cin>>str1>>str2>>tag>>radix;
// str1="1";
// str2="ab";
// tag=1;
// radix=2;

string num1,num2;
if(tag==1){
	num1=str1;
	num2=str2;
}else{
	num2=str1;
	num1=str2;
}

int tmp=num(num1,radix);
int minR = minRadix(num2);
for(int i=minR;i<36;i++){
	int anum = num(num2,i);
	if(anum==tmp){
		cout<<i;
		return 0;
	}else if(anum>tmp){
        cout<<"Impossible";
        return 0;
	}
}

}