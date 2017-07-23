package github.java.algorithm4.graph;

import java.util.HashMap;

public class SymbolGraph{
   private Graph G;
   private HashMap<String, Integer>st;
   private String[] keys;
   public SymbolGraph(String fileName,String sp){
	   st = new HashMap<String, Integer>(); 
	   In in = new In(fileName);
	   while(in.hasNextLine()){
		   String line = in.readLine();
		   String[] arr = line.split(sp);
		   for(int i=0;i<arr.length;i++){
			   st.put(arr[i], st.size());
		   }
	   }
	   keys = new String[st.size()];
	   for(String key : st.keySet()){
		   keys[st.get(key)] = key;
	   }
	   G = new Graph(st.size());
	   in = new In(fileName);
	   while(in.hasNextLine()){
		   String line = in.readLine();
		   String[] arr = line.split(sp);
		   int v = st.get(arr[0]);
		   for(int i=1;i<arr.length;i++){
			   int w = st.get(arr[i]);
			   G.addEdge(v, w);
		   }
	   }

   }
	
   public boolean contains(String key){
	   return st.containsKey(key);
   }

   public int index(String s){
	   return st.get(s);
   }

   public String name(int v){
	   return keys[v];
   }
   
   public Graph G(){
	   return G;
   }
   
   public String toString(){
	   return G.toString();
   }
   
	public static void main(String[] args) {
		String fileName = "C:\\Users\\sony\\Desktop/movies.txt";
        SymbolGraph graph = new SymbolGraph(fileName,"/");
        for(int j=0;j<graph.G.V();j++){
        	System.out.println(j);
            for(Integer i : graph.G.adj(j)){
            	System.out.print(i+",");
            }
            System.out.println();
        }

        
		
		
		
	}
	
	
	
	
	
}
