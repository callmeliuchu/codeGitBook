package github.java.algorithm4.graph;

import java.util.Iterator;

public class Queue<Item> implements Iterable<Item>{
    Node first,last;
	
	private class Node{
		Item item;
		Node next;
		Node(Item item){
			this.item = item;
			this.next = null;;
		}
	}
	
	public Queue(){
		first = last;
	}
	
	public void enqueue(Item item){
		Node node = new Node(item);
		if(last == null){
			first = last = node;
		}else{
			 last.next = node;
			 last = node;
		}
	}
	
	
	public Item dequeue(){
		Item item = first.item;
		first = first.next;
		return item;
	}
	
	public boolean isEmpty(){
		return first == null;
	} 
	
	
	
	
	public Iterator<Item> iterator() {
		// TODO Auto-generated method stub
		return new QueueIterator();
	}
	
	private class QueueIterator implements Iterator<Item>{
        private Node current;
        
        public QueueIterator(){
        	current = first;
        }
		public boolean hasNext() {
			return current != null;
		}

		public Item next() {
			Item item = current.item;
			current = current.next;
			return item;
		}

		public void remove() {
			
		}
		
	}
	
	public static void main(String[] args) {
		Integer[] arr = {1,12,334,2,3,3};
		Queue<Integer>q = new Queue<Integer>();
		for(int i=0;i<arr.length;i++){
			q.enqueue(arr[i]);
		}
	    while(!q.isEmpty()){
	    	int d = q.dequeue();
	    	System.out.println(d);
	    }
	}
	
	

}
