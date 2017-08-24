#include<iostream>
#include<vector>
#include<set>
using namespace std;
struct num{
   int e;
   float p;
};

int main(){
   int n;
   int e;
   float p;
   cin>>n;
   vector<struct num*>vec1;
   vector<float>vec(2002);
   for(int i=0;i<n;i++){
   	cin>>e>>p;
   	num *anum = new num();
   	anum->e=e;
   	anum->p=p;
    vec1.push_back(anum);
   } 
   cin>>n;
   for(int i=0;i<n;i++){
   	 cin>>e>>p;
      for(int j=0;j<vec1.size();j++){
      	  int index = e+vec1[j]->e;
          vec[index]+=p*vec1[j]->p;
      }
   } 
  int count=0;
   for(int i=2000;i>=0;i--){
      if(vec[i]!=0){
      	count++;
      }
   }  
  cout<<count;
   for(int i=2000;i>=0;i--){
      if(vec[i]!=0){
      	printf(" %d %.1f",i,vec[i]);
      }
   }
   cout<<endl;
}