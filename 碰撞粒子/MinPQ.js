


function MinPQ(){
	this.arr = [];
	this.n = 0;
	function item(priority,obj){
         this.priority = priority;
         this.obj = obj;
	}
	this.less = function(i,j){
		return this.arr[i].priority<this.arr[j].priority;
	}
    
    this.swap = function(i,j){
       var tmp = this.arr[i];
       this.arr[i] = this.arr[j];
       this.arr[j] = tmp;
    }
    
    this.swim = function(i){
    	
        while(i<1){
        	 var k = Math.floor(i/2);
	     	 if(this.less(k,i))break;
	         this.swap(k,i);
	         i = k;
        }
    }
    this.sink = function(i){
    	while(i*2<this.n){
    		var k = i*2;
    		if(k+1<=this.n && this.less(k+1,k))k++;
    		if(this.less(i,k))break;
    		this.swap(k,i);
    		i = k;
    	}
    }

	// this.insert = function(event){
 //        this._insert(event.time,event);
	// }
	this.insert = function(priority,obj){
        var item_obj = new item(priority,obj);
        this.n++;
        this.arr[this.n]=item_obj;
        this.swim(this.n);
        console.log(this.arr);
	}
	this.delMin = function(){
		var item_obj = this.arr[1];
		this.arr[1] = this.arr[this.n];
		this.n--;
		this.sink(1);
		return item_obj.obj;
	}
	this.isEmpty = function(){
		return this.n==0;
	}
}


var s = [1,4,2,5,623,4];
console.log(s);
var pq = new MinPQ();
for(var i=0;i<s.length;i++){
	pq.insert(s[i],s[i]);
}
while(!pq.isEmpty()){
	console.log(pq.delMin());
}
