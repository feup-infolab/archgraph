var Animal= require('./Animal.js');
var Mixin= require('./Mixin.js');


class Cao extends Animal{
  constructor(raca, name) {
      super(raca);
    this.name = name;
  }


  getName() {
    return this.name
  }
}
Object.assign(Cao.prototype, Mixin);
var cao =new Cao("raça","Dude") 

console.log(cao.getRaca());
cao.sayHi()// Hello Dude! 
//
console.log(Cao.prototype)

module.exports= Cao
