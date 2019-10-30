var Animal= require('./Animal.js');
var Mixin= require('./Mixin.js');


class Cao extends Animal{
    constructor(raca, name) {
        super(raca);
      this.name = name;
    }
  }

  function getName() {
      return this.name
  }
  Cao.prototype = Object.create(Animal.prototype);
  // copy the methods
  Object.assign(Cao.prototype, Mixin.mixin);
  
  // now User can say hi
  new Cao("Dude").sayHi(); // Hello Dude!

