package github.java.algorithm4.graph;

public class DirectedCycle{
	private Queue<Integer>cycle;
	private boolean[] marked;
	private int[] edgeTo;
	private boolean[] onStack;
	
	public boolean hasCycle(){
		return cycle!=null;
	}
	
	public DirectedCycle(Digraph G,int s){
		marked = new boolean[G.V()];
		onStack = new boolean[G.V()];
		edgeTo = new int[G.V()];
		
		for(int v=0;v<G.V();v++){
           if(!marked[v]){
        	   dfs(G,v);
           }
		}
		
	}
	
	
	private void dfs(Digraph G,int s){
		marked[s] = true;
		onStack[s] = true;
		for(Integer w : G.adj(s)){
			if(hasCycle()){
				return;
			}
			if(!marked[w]){
				edgeTo[w]=s;
				dfs(G,w);
			}else if(onStack[w]){
				cycle = new Queue<Integer>();
				for(int x=w;x!=s;x=edgeTo[x]){
					cycle.enqueue(x);
				}	
			}
		}
		onStack[s]=false;
		
	}
	
	
	
	
}
