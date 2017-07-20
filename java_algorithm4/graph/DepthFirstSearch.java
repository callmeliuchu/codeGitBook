package github.java.algorithm4.graph;

public class DepthFirstSearch {
    private boolean[] marked;
    private int count;
    
    public DepthFirstSearch(Graph G,int s){
    	marked = new boolean[G.V()];
    	dfs(G,s);
    }
	
    public void dfs(Graph G,int s){
    	count++;
    	marked[s] = true;
    	for(int w : G.adj(s)){
    		if(!marked[w]){
    			dfs(G,w);
    		}
    	}
    }
	public boolean marked(int w){
		return marked[w];
	}
	
	public int count(){
		return count;
	}
	
	
}
