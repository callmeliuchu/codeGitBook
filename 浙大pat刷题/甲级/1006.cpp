#include<iostream>
using namespace std;

struct dtime{
	string name;
	int hour;
	int minute;
	int second;
};

int cmp(struct dtime t1,struct dtime t2)
{
  if(t1.hour!=t2.hour){
  	return t1.hour<t2.hour;
  }else{
  	  if(t1.minute==t2.minute){
  	  	return t1.minute<t2.minute;
  	  }else{
  	  	return t1.second<t2.second;
  	  }
  }
  return 0;
}

int main(){
	
	string s;
	
	string stmax,stmin;
   struct dtime tmin,tmax;
	
	
	int a,b,c;
	int n;
	cin>>n;
	for(int i=0;i<n;i++){
	cin>>s;
//	cout<<s<<endl;
	scanf("%d:%d:%d",&a,&b,&c);
//	cout<<a<<" "<<b<<" "<<c<<endl;
	struct dtime enter=dtime();
	enter.name=s;
	enter.hour=a;
	enter.minute=b;
	enter.second=c;	
	
	scanf("%d:%d:%d",&a,&b,&c);
//	cout<<a<<" "<<b<<" "<<c<<endl;
	struct dtime leave=dtime();
	leave.name=s;
	leave.hour=a;
	leave.minute=b;
	leave.second=c;	
	
	
	
	if(i==0){
		tmin=enter;
		tmax=leave;
	}else{
		if(cmp(enter,tmin)){
			tmin=enter;
		}
		if(cmp(tmax,leave)){
			tmax=leave;
		}
		
	}
	
	}
   cout<<tmin.name<<" "<<tmax.name;
}
