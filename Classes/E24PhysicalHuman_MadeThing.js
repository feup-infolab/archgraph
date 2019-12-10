var E18PhysicalThing = require('./E18PhysicalThing.js');
var E71Human_MadeThing = require('./E71Human_MadeThing.js');


class E24PhysicalHuman_MadeThing extends E18PhysicalThing{
  constructor( P65, P156_occupies, P102) {
      super(P156_occupies);
    this.P65 = P65;
    this.P102 = P102
  }

  getP65() {
    return this.P65;
  }
}
Object.assign(E24PhysicalHuman_MadeThing.prototype, E71Human_MadeThing);
var E24 = new E24PhysicalHuman_MadeThing("property P65", "property P156_occupies", "property P102") 

console.log(E24.getP65()); // property P65
console.log(E24.getP102()); //property P102
console.log(E24.getP156_occupies()); //property P156_occupies

module.exports = E24PhysicalHuman_MadeThing
