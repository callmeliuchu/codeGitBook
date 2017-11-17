function print(obj){
	console.log(obj);
}

function  gcd(x,y){
   if(y == 0){
   	return x;
   }
   return gcd(y,x%y);
}

function genRanddomNum(){
	return Math.floor(Math.random()*10 + 6);
}
function example(){
		let x = genRanddomNum();
		let y = genRanddomNum();
		return new Number(x,y);
}

class Number{
	constructor(x,y){
		let flag = 1;
		if(x<0){
			x = -x;
			flag = -flag;
		}
		if(y<0){
			y = -y;
			flag = -flag;
		}
		let num = gcd(x,y);
		this.x = flag*(x/num);
		this.y = y/num;
	}
	plus(that){
       let y = this.y*that.y;
       let x = this.x*that.y + this.y*that.x;
       return new Number(x,y);
	}
	multiply(that){
       let x = this.x*that.x;
       let y = this.y*that.y;
       return new Number(x,y);
	}
	distract(that){
	   let y = this.y*that.y;
       let x = this.x*that.y - this.y*that.x;
       return new Number(x,y);
	}

	div(that){
		let x = this.x*that.y;
		let y = this.y*that.x;
		return new Number(x,y);
	}
    toString(){
    	return this.x + '/' + this.y;
    }
}

for(let i=0;i<10;i++){
	let num1 = example();
	let num2 = example();
	console.log(num1.toString() + " + " + num2.toString() + ' = ' + num1.plus(num2).toString());
	console.log(num1.toString() + " - " + num2.toString() + ' = ' + num1.distract(num2).toString());
	console.log(num1.toString() + " * " + num2.toString() + ' = ' + num1.multiply(num2).toString());
	console.log(num1.toString() + " / " + num2.toString() + ' = ' + num1.div(num2).toString());
	console.log('------------------------------------------------------------------------------');
}