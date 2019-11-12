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
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var protectedMethods = [];
function protect(target, propertyKey, descriptor) {
    var className = target.constructor.name;
    console.log(target.constructor);
    console.log(propertyKey);
    console.log(descriptor);
    protectedMethods.push(className + "." + propertyKey);
}
function enumerable(enumerable) {
    return function (target, propertyKey, propertyDescriptor) {
        console.log(propertyDescriptor);
        propertyDescriptor.enumerable = enumerable;
    };
}
var Families = /** @class */ (function () {
    function Families() {
        this.houses = ["Lannister", "Targaryen"];
    }
    Families.prototype.get = function () {
        return this.houses;
    };
    Families.prototype.post = function (request) {
        this.houses.push(request.body);
    };
    __decorate([
        enumerable(true)
    ], Families.prototype, "get");
    __decorate([
        protect
    ], Families.prototype, "post");
    return Families;
}());
console.log(protectedMethods); // ["Families.get", "Families.post"]
