#include<iostream>
#include<vector>
using namespace std;
int n,m,k;
vector<vector<int> >graph;
vector<int> visited;

void setToZero(){
	for(int i=1;i<=n;i++){
		visited[i]=0;
	}
}


void dfs(int v){
	visited[v]=1;
	for(int i=1;i<=n;i++){
		if(graph[v][i]==1 && visited[i]==0){
			dfs(i);
		}
	}
}

int count(int v){
	int c = 0;
	setToZero();
	visited[v]=1;
	for(int i=1;i<=n;i++){
		if(visited[i]==0){
		   c++;
		   dfs(i);
		}
    }
    return c;
}





int main(){
//3 2 3
//1 2
//1 3
//1 2 3

//n=3;
//m=2;
//k=3;
cin>>n>>m>>k;
graph.resize(n+1,vector<int>(n+1));
visited.resize(n+1);
//cin>>n>>m>>k;
int c1,c2;
//int arr[][2] = {{1,2},{1,3}};
for(int i=0;i<m;i++){
//	c1 = arr[i][0];
//	c2 = arr[i][1];
    cin>>c1>>c2;
 	graph[c1][c2]=graph[c2][c1]=1;
}
//int arr1[] = {1,2,3};
int c3;
for(int i=0;i<k;i++){
//	c3 = arr1[i];
    cin>>c3;
	cout<<count(c3)-1<<endl;
}




}
