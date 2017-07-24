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
      
      //this is for 4.1.2 S
      public Graph(Graph graph){
    	  this(graph.V);
    	  this.E = graph.E();
    	  for(int i=0;i<graph.V();i++){
    		  for(Integer v : graph.adj(i)){
    			   this.addSingleEdge(i, v);
    		  }
    	  }
      }
      private void addSingleEdge(int v,int w){
    	  adj[v].add(w);
      }  
      //this is for 4.1.2 E
      //this is for 4.14 S
      public boolean hasEdge(int v,int w){
    	  for(Integer i : adj[v]){
    		  if(i==w){
    			  return true;
    		  }
    	  }
    	  return false;
      }
      //this is for 4.14 E
      
      
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
		System.out.println(graph.hasEdge(7, 9));
//		Graph G = new Graph(graph);
//		System.out.println(G);
//        CC tool = new CC(graph);
//        System.out.println(tool);
	  }
      
}
