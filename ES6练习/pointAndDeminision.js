// class Point{
// 	constructor(...args){
// 		this.args = args;
// 	}
// 	// constructor(x,y){
// 	// 	this.x = x;
// 	// 	this.y = y;
// 	// }
// 	toString(){
// 		return "(" + this.x + "," + this.y + ")";
// 	}
// 	myPrint(text){
// 		console.log(text);
// 	}
// 	printName(x = '1.1'){
// 		this.myPrint(`hello ${x}`);
// 	}
// 	*[Symbol.iterator](){
// 		for(let arg of this.args){
// 			yield arg;
// 		}
// 	}
// }

// function selfish(target){
// 	const cache = new WeakMap();
// 	const handler = {
// 		get(target,key){
// 			const value = Reflect.get(target,key);
// 			if(typeof value !== 'function'){
// 				return value;
// 			}
// 			if(!cache.has(value)){
// 				cache.set(value,value.bind(target));
// 			}
// 			return cache.get(value);
// 		}
// 	};
// 	const proxy = new Proxy(target,handler);
// 	return proxy;
// }

// function Person(name){
// 	if(new.target === Person){
// 		this.name = name;
// 	}else{
// 		throw new Error('has to be new');
// 	}
// }

// var person = new Person('zhang san');

// const point = new Point(1,2);
// point.printName()
// const {printName} = point;
// printName();
// var point = new Point(1,2);
// var point2 = new Point(4,5);
// print(point.hasOwnProperty('x'))
// print(point.hasOwnProperty('y'))
// print(point.hasOwnProperty('toString'))
// print(point.__proto__.hasOwnProperty('toString'))
// print(point.__proto__ == point2.__proto__)
// print(Object.keys(Point.prototype))
// print(Object.getOwnPropertyNames(Point.prototype))
function print(obj){
	if(typeof obj.toString == 'function'){
       console.log(obj.toString());
	}else{
	   console.log(obj);
	}
}


class Point{
	constructor(x,y){
		this.x = x;
		this.y = y;
	}
	toString(){
		return '(' + this.x + ',' + this.y + ')';
	}
}

class Line{
	constructor(A,B,C){
		this.A = A;
		this.B = B;
		this.C = C;
	}
	getY(x){
		if(this.B==0){
		return Number.POSITIVE_INFINITY;
		}
		return (-this.C-this.A*x)/this.B;
	}
	getX(y){
		if(A==0){
		return Number.POSITIVE_INFINITY;
		}
		return (-this.B*y-this.C)/this.A;
	}
	toString(){
		return this.A + "*x + " + this.B +"*y + " + this.C + ' = 0';
	}
}

class Calculator{
    static generateLine(p1,p2){
    	let B = -(p1.x - p2.x);
    	let A = p1.y - p2.y;
    	let x = p1.x;
    	let y = p1.y;
    	let C = -(A*x+B*y);
    	return new Line(A,B,C);
    }
    static calDistancePToP(p1,p2){
    	let dx = p1.x - p2.x;
    	let dy = p1.y - p2.y;
    	return Math.sqrt(dx*dx + dy*dy);
    }
    static calDistancePToL(p,l){
    	return Math.abs(l.A*p.x+l.B*p.y+l.C)/Math.sqrt(l.A*l.A+l.B*l.B);
    }
    static calPointLWithL(l1,l2){
    	let common = l1.B*l2.A - l2.B*l1.A;
    	if(common == 0){
    		throw new Error('no point together');
    	}
    	let x = (l1.C*l2.B-l2.C*l1.B)/common;
    	let y = (l2.C*l1.A-l1.C*l2.A)/common;
    	return new Point(x,y);
    }
    static calDistanceLToL(l1,l2){
    	let common = l1.B*l2.A - l2.B*l1.A;
    	if(common != 0){
    		throw new Error('not parallel lines so no distance!');
    	}
    	if(l1.A==0 && l2.A==0){
    		return Math.abs(l1.C/l1.B-l2.C/l2.B);
    	}
    	if(l1.B==0 && l2.B==0){
    		return Math.abs(l1.C/l1.A-l2.C/l2.A);
    	}
    	let x0 = 0;
    	let y0 = l1.getY(x0);
    	let p = new Point(x0,y0);
    	return this.calDistancePToL(p,l2);
    }
}

var p1 = new Point(1,6);
var p2 = new Point(4,9);
var p3 = new Point(7,4);
var p4 = new Point(8,88);
var line1 = Calculator.generateLine(p1,p2);
var line2 = Calculator.generateLine(p4,p3);
var p = Calculator.calPointLWithL(line1,line2);