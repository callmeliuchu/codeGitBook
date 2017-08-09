#include<iostream>
#include<vector>
#include<queue>
using namespace std;
vector<vector<int> >tree(101);
vector<int>res;


int levelOrder(){
	queue<int>q;
	q.push(1);
	int count=0;
	while(!q.empty()){
          int len=q.size();
          int count=0;
          for(int i=0;i<len;i++){
          	int p=q.front();
          	q.pop();
          	int size=tree[p].size();
          	if(size==0){
          	  count++;
          	}
          	for(int j=0;j<size;j++){
          		q.push(tree[p][j]);
          	}
          }
          res.push_back(count);
	}
}

int main(){
	int n,m;
	cin>>n>>m;

	int id,k,c;
	for(int i=0;i<m;i++){
		cin>>id>>k;
		for(int j=0;j<k;j++){
			cin>>c;
			tree[id].push_back(c);
		}
	}
	levelOrder();
	for(int i=0;i<res.size();i++){
		if(i==0){
			cout<<res[i];
		}else{
			cout<<" "<<res[i];
		}
	}
	
}
