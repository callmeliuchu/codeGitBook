


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

	this.insert = function(event){
        this._insert(event.time,event);
	}
	this._insert = function(priority,obj){
        var item_obj = new item(priority,obj);
        this.n++;
        for(var i=1;i<)
	}
	this.delMin = function(){
		
	}
	this.isEmpty = function(){
		return this.arr.length==0;
	}
}


// var s = [1,4,2,5,623,4];
// var pq = new MinPQ();
// for(var i=0;i<s.length;i++){
// 	pq.insert(s[i],s[i]);
// }
// while(!pq.isEmpty()){
// 	console.log(pq.delMin());
// }
