package github.java.algorithm4.graph;

public class DepthFirstPaths {
	private boolean[] marked;
	private final int s;
	private int[] edgeTo;
	
	public DepthFirstPaths(Graph graph,int s){
		this.s = s;
		marked = new boolean[graph.V()];
		edgeTo = new int[graph.V()];
		dfs(graph,s);
	}
	
	public void dfs(Graph graph,int s){
		marked[s] = true;
		for(int v : graph.adj(s)){
			if(!marked[v]){
				edgeTo[v]=s;
				dfs(graph,v);
			}
		}
	}
	
	public Iterable<Integer>paths(int v){
		Bag<Integer>path = new Bag<Integer>();
		for(int w=v;w!=s;w=edgeTo[w]){
			path.add(w);
		}
		path.add(s);
		return path;
	}
	
	
	
}
