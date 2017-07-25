package github.java.algorithm4.graph;

public class Digraph {
    private int E;
    private int V;
    private Bag<Integer>[] adj;
    public Digraph(int V){
    	this.V = V;
    	E = 0;
    	adj = (Bag<Integer>[])new Bag[V];
    	for(int i=0;i<V;i++){
    		adj[i] = new Bag<Integer>();
    	}
    }
    
    public void addEdge(int v,int w){
    	adj[v].add(w);
    	E++;
    }
    
    public Iterable<Integer> adj(int v){
    	return adj[v];
    }
    
    public Digraph reverse(){
    	Digraph G = new Digraph(V);
    	for(int v=0;v<V;v++){
    		for(Integer w : adj(v)){
    			G.addEdge(w, v);
    		}
    	}
    	return G;
    }
    public String toString(){
    	StringBuffer sb = new StringBuffer();
    	sb.append("V:").append(V).append(",").append("E:").append(E).append("\n");
    	for(int v = 0;v<V;v++){
    		sb.append(v).append("\n");
    		for(Integer w : adj(v)){
    			sb.append(w).append(" ");
    		}
    	}
    	return sb.toString();
    }
    public Digraph(In in){
    	this(in.readInt());
    	int E = in.readInt();
        for(int i=0;i<E;i++){
        	int v = in.readInt();
        	int w = in.readInt();
        	this.addEdge(v, w);
        }
    }
    
    
    
    public static void main(String[] args) {
		In in = new In("C:\\Users\\sony\\Desktop\\tinyG.txt");
		Digraph graph = new Digraph(in);
		System.out.println(graph);
    	
	}
    
    
}
