package github.java.algorithm4.graph;

public class EdgeWeightedDigraph {
    private final int V;
    private int E;
    private Bag<DirectedEdge>[] adj;
    
    public  EdgeWeightedDigraph(int V){
    	this.V = V;
    	this.E = 0;
    	adj = (Bag<DirectedEdge>[])new Bag[V];
    	for(int i=0;i<V;i++){
    		adj[i] = new Bag<DirectedEdge>();
    	}
    }
	
    
    public void  addEdge(DirectedEdge e){
    	adj[e.from()].add(e);
    	E++;
    }
    
    public Iterable<DirectedEdge> adj(int v){
    	return adj[v];
    }
    
    public Iterable<DirectedEdge> edges(){
    	Bag<DirectedEdge>list = new Bag<DirectedEdge>();
    	for(int v=0;v<V;v++){
    		for(DirectedEdge e : adj[v]){
    			list.add(e);
    		}
    	}
    	return list;
    }
	
	
}
