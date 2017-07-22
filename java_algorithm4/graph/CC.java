package github.java.algorithm4.graph;

public class CC {
    private boolean[] marked;
    private int count;
    private int[] id;
    
    public CC(Graph G){
    	id = new int[G.V()];
    	marked = new boolean[G.V()];
    	for(int i=0;i<G.V();i++){
    		if(!marked[i]){
    			dfs(G,i);
    			count++;
    		}
    	}
    }
    
    private void dfs(Graph G,int s){
    	marked[s] = true;
    	id[s] = count;
    	for(Integer v : G.adj(s)){
    		if(!marked[v]){
    			dfs(G,v);
    			marked[v]=true;
    		}
    	}
    }
    
    public String toString(){
    	StringBuffer sb = new StringBuffer();
    	for(int i=0;i<id.length;i++){
    		sb.append(i).append(":").append(id[i]).append("\n");
    	}
    	return sb.toString();
    }
    
	
	
	
}
