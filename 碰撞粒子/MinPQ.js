


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
        while(i>1){
        	 var k = Math.floor(i/2);
	     	 if(this.less(k,i))break;
	         this.swap(k,i);
	         i = k;
        }
    }
    this.sink = function(i){
    	while(i*2<=this.n){
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

<<<<<<< HEAD
var s = [1,2,4,2,3,2,323,2,33,24,34,4,2,32,4,435,34,53,45,345,435,345,534,534,345,345,345,345,345,345,34];
=======

var s = [1,4,2,5,623,4,4,5,678,423,234,234,234,234,234234,234];
console.log(s);
>>>>>>> b59ccbda68f6195a858db02dda23ecb962a91428
var pq = new MinPQ();
for(var i=0;i<s.length;i++){
	pq.insert(s[i],s[i]);
}
var str = "";
while(!pq.isEmpty()){
    str = str + pq.delMin() + ",";
	// console.log(pq.delMin());
}
console.log(str);
