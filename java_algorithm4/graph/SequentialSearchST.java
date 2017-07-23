package github.java.algorithm4.graph;

public class SequentialSearchST<Key,Value>{
    private Node first;
    private int size;
    
    public Value get(Key key){
    	for(Node p=first;p!=null;p=p.next){
    		if(key.equals(p.key)){
    			return p.value;
    		}
    	}
    	return null;
    }
    
    public int size(){
    	return size;
    }
    
    
    
    
    public void put(Key key,Value val){
    	for(Node p=first;p!=null;p=p.next){
    		if(key.equals(p.key)){
    			p.value = val;
    			return;
    		}
    	}    
    	Node oldFirst = first;
    	first = new Node(key,val);
    	first.next = oldFirst;
    	size++;
    }
    
	private class Node{
		Node next;
		Key key;
		Value value;
		Node(Key key,Value val){
			this.key = key;
			this.value = val;
			this.next = null;
		}
	}
	
	
  public static void main(String[] args) {
	Integer[] arr = {1,23,4,1,4,12,4};
	SequentialSearchST<Integer,Integer>st = new SequentialSearchST<Integer, Integer>();
	for(int i=0;i<arr.length;i++){
		st.put(i,arr[i]);
	}
	  
}
	
	
}
