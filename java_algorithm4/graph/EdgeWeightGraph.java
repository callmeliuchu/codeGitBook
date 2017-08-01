package github.java.algorithm4.graph;

public class EdgeWeightGraph {
	private int V;
	private int E;
    private Bag<Edge>[] adj;
    
    
    public EdgeWeightGraph(int V){
    	this.V = V;
    	this.E = 0;
    	adj = (Bag<Edge>[])new Bag[V];
    	for(int v=0;v<V;v++){
    		adj[v] = new Bag<Edge>();
    	}
;    }
	
    public EdgeWeightGraph(In in){
    	this(in.readInt());
    	int E = in.readInt();
    	for(int i=0;i<E;i++){
    		int v = in.readInt();
    		int w = in.readInt();
    		double weight = in.readDouble();
    		Edge e = new Edge(v,w,weight);
    		addEdge(e);
    	}
    }
    
    public void addEdge(Edge e){
    	int v = e.either();
    	int w = e.other(v);
    	adj[v].add(e);
    	adj[w].add(e);
    	E++;
    }
    
    public Iterable<Edge> adj(int v){
    	return adj[v];
    }
    
    
    
	
    public String toString(){
    	StringBuffer sb = new StringBuffer();
    	sb.append("V:").append(V).append("\n")
    	  .append("E:").append(E).append("\n");
    	for(int i=0;i<V;i++){
    	sb.append(i).append(":");
    		for(Edge e : adj(i)){
    			sb.append(e).append(",");
    		}
    	sb.append("\n");
    	}
    	return sb.toString();
    }
    
    
    public static void main(String[] args) {
		String path = "C:\\Users\\sony\\Desktop\\tinyEWG.txt";
		In in = new In(path);
		EdgeWeightGraph G = new EdgeWeightGraph(in);
        System.out.println(G);
	}
	
	
	
	
}
