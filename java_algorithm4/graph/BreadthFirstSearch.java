package github.java.algorithm4.graph;

public class BreadthFirstSearch {
   private boolean[] marked;
   private int[] edgeTo;
   private final int s;
   
   public BreadthFirstSearch(Graph G,int s){
	    this.s = s;
	    edgeTo = new int[G.V()];
	    marked = new boolean[G.V()];
	    bfs(G,s);
   }
   

   private void bfs(Graph G,int s){
	   marked[s] = true;
	   Queue<Integer>q = new Queue<Integer>();
	   q.enqueue(s);
	   while(!q.isEmpty()){
		   int w = q.dequeue();
		   for(Integer v : G.adj(w)){
			   if(!marked[v]){
				   edgeTo[v] = w;
				   marked[v] = true;
				   q.enqueue(v);
			   }
		   }
	   }
   }

   public boolean hasPathTo(int v){
	   return marked[v];
   }
   
   public Iterable<Integer> pathTo(int v){
	   Queue<Integer>q = new Queue<Integer>();
	   for(int w=v;w!=s;w=edgeTo[w]){
		   q.enqueue(w);
	   }
	   q.enqueue(s);
	   return q;
   }
   
   public static void main(String[] args) {
	
}
	
	
}
