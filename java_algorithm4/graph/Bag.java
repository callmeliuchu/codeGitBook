package github.java.algorithm4.graph;

import java.util.Iterator;


public class Bag<Item> implements Iterable<Item>{
    private Node first;
	
	private class Node{
		Item item;
		Node next;
	}
	
	public Bag(){
		first = null;
	}
	
	public void add(Item item){
       Node oldFirst = new Node();
       oldFirst.item = item;
       oldFirst.next = first;
       first = oldFirst;
	}
	
	public boolean isEmpty(){
         return first == null;
	}
	
	
	
	
	public Iterator<Item> iterator() {
		return new BagIterator();
	}
	
	private class BagIterator implements Iterator<Item>{
        Node current =  first;
		public boolean hasNext() {
			return current!=null;
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
		Integer[] arr = {1,32,4,23,4,23,4};
		Bag<Integer>bag = new Bag<Integer>();
		for(int i=0;i<arr.length;i++){
			bag.add(arr[i]);
		}
		for(Integer i : bag){
			System.out.println(i);
		}
	}


}
