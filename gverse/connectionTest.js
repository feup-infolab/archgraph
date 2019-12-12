//var OrientDB = require('orientjs');
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __generator = (this && this.__generator) || function (thisArg, body) {
    var _ = { label: 0, sent: function() { if (t[0] & 1) throw t[1]; return t[1]; }, trys: [], ops: [] }, f, y, t, g;
    return g = { next: verb(0), "throw": verb(1), "return": verb(2) }, typeof Symbol === "function" && (g[Symbol.iterator] = function() { return this; }), g;
    function verb(n) { return function (v) { return step([n, v]); }; }
    function step(op) {
        if (f) throw new TypeError("Generator is already executing.");
        while (_) try {
            if (f = 1, y && (t = op[0] & 2 ? y["return"] : op[0] ? y["throw"] || ((t = y["return"]) && t.call(y), 0) : y.next) && !(t = t.call(y, op[1])).done) return t;
            if (y = 0, t) op = [op[0] & 2, t.value];
            switch (op[0]) {
                case 0: case 1: t = op; break;
                case 4: _.label++; return { value: op[1], done: false };
                case 5: _.label++; y = op[1]; op = [0]; continue;
                case 7: op = _.ops.pop(); _.trys.pop(); continue;
                default:
                    if (!(t = _.trys, t = t.length > 0 && t[t.length - 1]) && (op[0] === 6 || op[0] === 2)) { _ = 0; continue; }
                    if (op[0] === 3 && (!t || (op[1] > t[0] && op[1] < t[3]))) { _.label = op[1]; break; }
                    if (op[0] === 6 && _.label < t[1]) { _.label = t[1]; t = op; break; }
                    if (t && _.label < t[2]) { _.label = t[2]; _.ops.push(op); break; }
                    if (t[2]) _.ops.pop();
                    _.trys.pop(); continue;
            }
            op = body.call(thisArg, _);
        } catch (e) { op = [6, e]; y = 0; } finally { f = t = 0; }
        if (op[0] & 5) throw op[1]; return { value: op[0] ? op[1] : void 0, done: true };
    }
};
var ODatabase = require('orientjs').ODatabase;
var db = new ODatabase({
    host: 'localhost',
    port: 2424,
    username: 'root',
    password: 'root',
    name: 'DatabaseGraph'
});
/*

//getting class
var player = db.class.get('Player')
.then(function(player){
    console.log('Retrieved class: ' + player.name);

    //addProporty
    player.property.create({
      name: 'name',
      type: 'String'
    },
    {
      name: 'idade',
      type: 'Integer'
    })
    .then(function(property){
        console.log("Created Property: " + property.name);
    })
    .catch(function(error){
        console.log(error.message)
    });

    //add player
    player.create({
    name: "Ty Cobb",
    idade: 12
    })
    .then(
      function(player){
        console.log('Created Record: ', player.name);
    })
    .catch(
        function(error){
          console.log("Didn't create Record: ", error.message);
    });
})
.catch(function(error){
  console.log(error.message)
});

//updatting class
db.class.update({
  name: 'Player',
  superClass: 'V'
})
.then(function(player){
  console.log(
    'Updated Class: ' + player.name
    + ' to extend ' + player.superClass
  );
})
.catch(function(error){
  console.log(error.message)
});



//query
var idade = 10;
var hitters = db.query(
  'SELECT * FROM Player WHERE idade >= :idade ',
  {params: {
    idade: idade,
  },limit: 20 }
)
.then(function(players){
  console.log(players);
})
.catch(function(error){
  console.log(error.message)
})
*/
function func() {
    return __awaiter(this, void 0, void 0, function () {
        var result, _a, _b, _c, _d, _e, _f, _g, _h;
        return __generator(this, function (_j) {
            switch (_j.label) {
                case 0:
                    result = [];
                    //create class
                    _b = (_a = result).push;
                    return [4 /*yield*/, db["class"].create('player', 'V')];
                case 1:
                    //create class
                    _b.apply(_a, [_j.sent()]);
                    _d = (_c = result).push;
                    return [4 /*yield*/, db["class"].create('player1', 'V')];
                case 2:
                    _d.apply(_c, [_j.sent()]);
                    //get classes
                    console.log('getClasses');
                    _f = (_e = result).push;
                    return [4 /*yield*/, db["class"].get('player')];
                case 3:
                    _f.apply(_e, [_j.sent()]);
                    _h = (_g = result).push;
                    return [4 /*yield*/, db["class"].get('player1')];
                case 4:
                    _h.apply(_g, [_j.sent()]);
                    //close database
                    return [4 /*yield*/, db.close()];
                case 5:
                    //close database
                    _j.sent();
                    return [2 /*return*/, result];
            }
        });
    });
}
func()
    .then(function (result) {
    result.forEach(function (element) {
        console.log(element.name);
    });
})["catch"](function (error) {
    console.log(error.message);
    db.close();
});
