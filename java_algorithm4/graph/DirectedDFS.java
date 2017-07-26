package github.java.algorithm4.graph;

public class DirectedDFS {
    private boolean[]  marked;
    
    public DirectedDFS(Digraph G,int s){
    	marked = new boolean[G.V()];
    	dfs(G,s);
    }
    
	public DirectedDFS(Digraph G,Iterable<Integer> source){
		marked = new boolean[G.V()];
		for(Integer v : source)
		if(!marked[v]){
			dfs(G,v);
		}
	}
	
   private void dfs(Digraph G,int s){
	   marked[s] = true;
	   for(Integer v : G.adj(s)){
		   if(!marked[v]){
			   dfs(G,v);
		   }
	   } 
   }
   
   public boolean marked(int v){
	   return marked[v];
   }
	
	
}
