package github.java.algorithm4.graph;

public class WeightedQuickUnionUF {
    private int[] id;
    private int[] sz;
    private int count;
    
    
    public WeightedQuickUnionUF(int size){
    	count = size;
    	id = new int[size];
    	for(int i=0;i<size;i++){
    		id[i]=i;
    	}
    	sz = new int[size];
    	for(int i=0;i<size;i++){
    		sz[i]=1;
    	}
    }
    
    public int count(){
    	return count;
    }
	
    public boolean connected(int p,int q){
    	return find(p)==find(q);
    }
    
    private int find(int p){
    	while(id[p]!=p)p=id[p];
    	return p;
    }
    
    public void union(int p,int q){
    	int i = find(p);
    	int j = find(q);
    	if(i==j)return;
    	if(sz[i]<sz[j]){
    		id[i]=j;
    		sz[j]=sz[j]+sz[i];
    	}else{
    		id[j]=i;
    		sz[i]=sz[i]+sz[j];
    	}
    	count--;
    }
    
    
    
    
	
}
