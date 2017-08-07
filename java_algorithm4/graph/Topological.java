package github.java.algorithm4.graph;

public class Topological {
    private Iterable<Integer>order;
    public Iterable<Integer>order(){
    	return order;
    }
	
    public Topological(EdgeWeightedDigraph G){
    	DepthFirstOrder dp = new DepthFirstOrder(G);
    	order = dp.reversePost();
    }
	
	
}
