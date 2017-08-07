package github.java.algorithm4.graph;

public class DepthFirstOrder {
    private boolean[] marked;
    private Queue<Integer>pre;
    private Queue<Integer>post;
    private Stack<Integer>reversePost;
    
    
    public DepthFirstOrder(EdgeWeightedDigraph G){
    	marked = new boolean[G.V()];
    	pre = new Queue<Integer>();
    	post = new Queue<Integer>();
    	reversePost = new Stack<Integer>();
    	for(int v=0;v<G.V();v++){
    		dfs(G,v);
    	}
    }
	
    private void dfs(EdgeWeightedDigraph G,int v){
    	pre.enqueue(v);
    	marked[v] = true;
    	for(DirectedEdge e : G.adj(v)){
    		int w =  e.to();
    		if(!marked[w]){
    			dfs(G,w);
    		}
    	}
    	post.enqueue(v);
    	reversePost.push(v);
    }
    
    public Iterable<Integer>pre(){
    	return pre;
    }
    
    public Iterable<Integer>post(){
    	return post;
    }
	
    public Iterable<Integer>reversePost(){
    	return reversePost;
    }
	
}
