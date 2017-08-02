package github.java.algorithm4.graph;

public class LazyPrimMST {
    private MinPQ<Edge> pq;
    private boolean[] marked;
    private Queue<Edge> mst;
    
    
    public LazyPrimMST(EdgeWeightGraph G){
    	   pq = new MinPQ<Edge>();
    	   marked = new boolean[G.V()];
    	   mst = new Queue<Edge>();
    	   visited(G,0);
    	   
    	   while(!pq.isEmpty()){
    		   Edge e = pq.delMin();
    		   int w = e.either();
    		   int v = e.other(w);
    		   if(marked[w] && marked[v])continue;
    		   mst.enqueue(e);
    		   if(!marked[w])visited(G,w);
    		   if(!marked[v])visited(G,v);
    	   }
    	   
    } 
    
    public Iterable<Edge> edges(){
    	return mst;
    }
    private void visited(EdgeWeightGraph G,int v){
    	marked[v] = true;
    	for(Edge e : G.adj(v)){
    		if(!marked[e.other(v)]){
    			pq.insert(e);
    		}
    	}
    }
    
    public static void main(String[] args) {
		String path = "C:\\Users\\sony\\Desktop\\tinyEWG.txt";
		In in = new In(path);
		EdgeWeightGraph G = new EdgeWeightGraph(in);
		System.out.println(G);
		LazyPrimMST mst = new LazyPrimMST(G);
		Iterable<Edge> q = mst.edges();
		for(Edge e : q){
			System.out.println(e);
		}
		
	}
    
	
	
	
}
