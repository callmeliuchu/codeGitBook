package github.java.algorithm4.graph;

public class Edge implements Comparable<Edge>{
    private  int v;
    private int w;
    private double weight;
    
    public double weight(){
    	return weight;
    }
    
    public int other(int vertex){
    	if(vertex==v){
    		return w;
    	}else if(vertex==w){
    		return v;
    	}
    	return -1;
    }
    
    public int either(){
    	return v;
    }
    
    public Edge(int v,int w,double weight){
    	this.v = v;
    	this.w = w;
    	this.weight = weight;
    }
	
	public int compareTo(Edge that) {
		if(this.weight < that.weight){
			return -1;
		}else if(this.weight > that.weight){
			return 1;
		}
		return 0;
	}
	
	public String toString(){
		return v + "=>"  + w + ":"  + weight ;
	}

}
