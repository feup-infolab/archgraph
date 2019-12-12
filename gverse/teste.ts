/*

function decorator1(target){   
    console.log(target)
    Object.defineProperty(target.prototype, 'course', {value: ()=> "angular"})
    target.a = "qqqq"
}
function nova (decorator){
    return function(target){
        Object.defineProperty(target.prototype, 'course', {value: ()=> decorator.a})

    }
}

@nova({
    a:"ola"
})
class Point {
    public id: string
    private _x: number;
    private _y: number;
    public a : string
    constructor(x: number, y: number, id:string) {
        this._x = x;

        this._y = y;
        this.id = id
    }

}

var x = new Point(1,2, 'as')
console.log(x.course())
*/

const protectedMethods = [];

function protect(target, propertyKey, descriptor) {
  const className = target.constructor.name;
  console.log(target.constructor )
  console.log(propertyKey)
  console.log(descriptor)
  protectedMethods.push(className + "." + propertyKey);
}

function enumerable(enumerable: boolean) {
  return (
     target: Families,
     propertyKey: string,
     propertyDescriptor: PropertyDescriptor
  ) => {
    console.log(propertyDescriptor)
     propertyDescriptor.enumerable = enumerable;
  }
}

class Families {
  private houses = ["Lannister", "Targaryen"];

  @enumerable(true)
  get() {
    return this.houses;
  }
  
  @protect
  post(request) {
    this.houses.push(request.body);
  }
}

console.log(protectedMethods) // ["Families.get", "Families.post"]



class Animal {
  public raca:string;
  protected listType: Array<string>;
  constructor( raca:string){
    this.listType = ['qw']

  }
  getList(){
    return this.listType
  }
  @addType
  addEle(){}

}

function addType(target, propertyKey, descriptor) {

  var x  = target.constructor.name
  console.log(target.getList.value)
  return 
  
  }

  function deco(target, propertyKey, descriptor) {
    console.log(target)
    
    }


class Cao extends Animal{
  constructor( name:string, raca:string){
  super(raca)
  this.listType.push('q')

}

@deco
func(){
}

}

var x = new Cao('name', 'raca')
console.log(x.getList())


