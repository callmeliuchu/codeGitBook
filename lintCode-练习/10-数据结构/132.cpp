#include<iostream>
#include<vector>
using namespace std;


int main(){
// doaf
// agai
// dcan
   vector<vector<char> >matrix;
   string  strArr[3] = {"doaf","agai","dcan"};
     
     for(int i=0;i<3;i++){
       vector<char> vec;
       for(int j=0;j<strArr[i].length();i++){
       	  vec.push_back(strArr[i][j]);
       }
   	   matrix.push_back(vec);
     }



}