package github.java.algorithm4.graph;

public class DijkstraSP {
    private DirectedEdge[] edgeTo;
    private double[]  distTo;
    private IndexMinPQ<Double> pq;
    
    public DijkstraSP(EdgeWeightedDigraph G,int s){
    	edgeTo = new DirectedEdge[G.V()];
    	distTo = new double[G.V()];
    	pq = new IndexMinPQ<Double>(G.V());
    	for(int v=0;v<G.V();v++){
    		distTo[v] = Double.POSITIVE_INFINITY;
    	}
    	distTo[s] = 0.0;
    	pq.insert(s,0.0);
    	while(!pq.isEmpty()){
    		relax(G,pq.delMin());
    	}
    	
   }
    
    private void relax(EdgeWeightedDigraph G,int v){
      for(DirectedEdge e : G.adj(v)){
    	  int w = e.to();
    	  if(distTo[w]>e.weight()+distTo[v]){
    		  distTo[w]=e.weight()+distTo[v];
    		  edgeTo[w]=e;
    		  if(pq.contains(w))pq.change(w, distTo[w]);
    		  else{
    			  pq.insert(w, distTo[w]);
    		  }
    	  }
      }
    }
    
    
	
	
	
}
