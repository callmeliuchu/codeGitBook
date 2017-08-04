package github.java.algorithm4.graph;

public class KrusKalMST {
    private MinPQ<Edge> pq;
    private WeightedQuickUnionUF uf;
    private Queue<Edge>mst;
    
    
    public KrusKalMST(EdgeWeightGraph G){
    	pq = new MinPQ<Edge>();
    	uf = new WeightedQuickUnionUF(G.V());
    	for(Edge e : G.edges()){
    		pq.insert(e);
    	}
    	while(!pq.isEmpty() && mst.size()<G.V()-1){
    		Edge e = pq.delMin();
    		int w = e.either();
    		int v = e.other(w);
    		if(uf.connected(v, w)){
    			continue;
    		}
    		uf.union(w, v);
    		mst.enqueue(e);
    	}
    }
	
    public Iterable<Edge> edges(){
    	return mst;
    }
	
	
}
