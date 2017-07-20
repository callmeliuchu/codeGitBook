package github.java.algorithm4.graph;

public class Graph {
      private int V;
      private int E;
      private Bag<Integer>[] adj;
      public Graph(int V){
    	  this.V = V;
    	  this.E = 0;
    	  adj = (Bag<Integer>[]) new Bag[V];
    	  for(int i=0;i<V;i++){
    		  adj[i] = new Bag<Integer>();
    	  }
      }
      public int E(){
    	  return E;
      }
      public int V(){
    	  return V;
      }
      public void addEdge(int v,int w){
    	  adj[w].add(v);
    	  adj[v].add(w);
    	  E++;
      }
      public Graph(In in){
    	  this(in.readInt());
    	  int E = in.readInt();
    	  for(int i=0;i<E;i++){
    		  int v = in.readInt();
    		  int w = in.readInt();
    		  addEdge(v,w);
    	  }
      }
      public Iterable<Integer>adj(int v){
    	  return adj[v];
      }
      
      public String toString(){
    	  String s = "";
    	  s = "E:" + this.E + "," + "V:" + this.V + "\n";
    	  for(int i=0;i<V;i++){
    		  s = s + i + ":";
    		  for(Integer v : adj[i]){
    			  s = s + v + " ";
    		  }
    		  s = s + "\n";
    	  }
    	  return s;
      }
      
      
      
      public static void main(String[] args) {
		In in = new In("C:\\Users\\sony\\Desktop\\tinyG.txt");
		Graph graph = new Graph(in);
		System.out.println(graph);
		DepthFirstPaths tool = new DepthFirstPaths(graph,3);
		for(Integer i : tool.paths(0)){
			System.out.print(i+",");
		}
	  }
      
}
