#include<iostream>
#include<vector>
using namespace std;
int n,m,c1,c2;
vector<int>visited(500);
vector<vector<int> >graph(500,vector<int>(500));
vector<int>w;
//int w[]={1,2,1,5,3};
int totalW = 0;
int totalDis = 0;
int count=0;
int resW=-1;
int resDis = 1000000;

void dfs(int s){
	if(s==c2){
		if(resDis>totalDis){
			resDis=totalDis;
			resW = totalW;
			count=1;
		}else if(resDis==totalDis){
			if(resW<totalW){
				resW=totalW;
			}
			count++;
		}
	return;
	}
	for(int i=0;i<n;i++){
		if(graph[s][i] && visited[i]==0){
			visited[i]=1;
			totalW = totalW + w[i];
			totalDis = totalDis + graph[s][i];
			dfs(i);
			totalDis = totalDis - graph[s][i];
			totalW = totalW - w[i];
			visited[i]=0;
		}
	}
}




int main(){
//n=5;
//m=6;
//c1=0;
//c2=2;
cin>>n>>m>>c1>>c2;
int num;
for(int i=0;i<n;i++){
	cin>>num;
	w.push_back(num);
}
//graph[0][1]=graph[1][0]=1;
//graph[0][2]=graph[2][0]=2;
//graph[0][3]=graph[3][0]=1;
//graph[1][2]=graph[2][1]=1;
//graph[2][4]=graph[4][2]=1;
//graph[3][4]=graph[4][3]==1;
int p1,p2,d;
for(int i=0;i<m;i++){
	cin>>p1>>p2>>d;
	graph[p1][p2]=graph[p2][p1]=d;
}
visited[c1]=1;
totalW=w[c1];
dfs(c1);
cout<<count<<" "<<resW;
}
