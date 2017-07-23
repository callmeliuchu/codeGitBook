package github.java.algorithm4.graph;

public class SeparateChainingHashST<Key,Value>{
    private int N;
    private int M;
    private Bag<Key> bag;
	private SequentialSearchST<Key, Value>[] st;
	
	public SeparateChainingHashST(){
		this(997);
	}
	
	public SeparateChainingHashST(int M){
		this.M = M;
		bag = new Bag<Key>();
		st = (SequentialSearchST<Key, Value>[])new SequentialSearchST[M];
		for(int i=0;i<M;i++){
			st[i] = new SequentialSearchST<Key,Value>();
		}
	}
	private int hash(Key key){
		return (key.hashCode() & 0x7fffffff)%M;
	}
	public void put(Key key,Value val){
		Value  value = get(key);
		if(value==null){
			N++;
			bag.add(key);
		}
		st[hash(key)].put(key, val);
	}
	public int size(){
		return N;
	}
	public Value get(Key key){
		return (Value)st[hash(key)].get(key);
	}
	public Iterable<Key> keys(){
		return bag;
	}
	
	public boolean contains(Key key){
		return get(key)!=null;
	}
	
	
	public static void main(String[] args) {
		SeparateChainingHashST<String, String>ST = new SeparateChainingHashST<String, String>();
		ST.put("hello", "World");
		ST.put("hello", "World1");
		System.out.println(ST.get("hello"));
		for(String key : ST.keys()){
			System.out.println(key);
		}
	}
	
}
