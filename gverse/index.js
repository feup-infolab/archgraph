<<<<<<< HEAD
"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
Object.defineProperty(exports, "__esModule", { value: true });
const gverse_1 = require("gverse");
const graph = new gverse_1.default.Graph(new gverse_1.default.Connection({ host: "localhost", port: 9080, debug: true }));
class User extends gverse_1.default.Vertex {
    constructor() {
        super(...arguments);
        this.type = "User";
        this.name = "";
    }
}
class Repo {
}
function createUser() {
    return __awaiter(this, void 0, void 0, function* () {
        let user = new User();
        user.name = "Zak";
        yield graph.create(user);
    });
}
function getUser(uid) {
    return __awaiter(this, void 0, void 0, function* () {
        const user = (yield graph.get(User, uid));
        console.log(user.name); // = "Zak"
    });
}
createUser();
//# sourceMappingURL=index.js.map
=======
var OrientDB = require('orientjs');
var ODatabase = require('orientjs').ODatabase;
var db = new ODatabase({
    host: 'localhost',
    port: 2424,
    username: 'root',
    password: 'root',
    name: 'DatabaseGraph'
});
//create class
db["class"].create('Player', 'V')
    .then(function (player) {
    console.log('Created Vertex Class: ' + player.name);
})["catch"](function (error) {
    console.log("Didn't create class:", error.message);
});
//getting class
var player = db["class"].get('Player')
    .then(function (player) {
    console.log('Retrieved class: ' + player.name);
    //addProporty
    player.property.create({
        name: 'name',
        type: 'String'
    }, {
        name: 'idade',
        type: 'Integer'
    })
        .then(function (property) {
        console.log("Created Property: " + property.name);
    })["catch"](function (error) {
        console.log(error.message);
    });
    //add player
    player.create({
        name: "Ty Cobb",
        idade: 12
    })
        .then(function (player) {
        console.log('Created Record: ', player.name);
    })["catch"](function (error) {
        console.log("Didn't create Record: ", error.message);
    });
})["catch"](function (error) {
    console.log(error.message);
});
//updatting class
db["class"].update({
    name: 'Player',
    superClass: 'V'
})
    .then(function (player) {
    console.log('Updated Class: ' + player.name
        + ' to extend ' + player.superClass);
})["catch"](function (error) {
    console.log(error.message);
});
//query
var idade = 10;
var hitters = db.query('SELECT * FROM Player WHERE idade >= :idade ', { params: {
        idade: idade
    }, limit: 20 }).then(function (players) {
    console.log(players);
});
//close database
/*
  db.close()
.then(function(){
  console.log('closed');
});
});*/
>>>>>>> master
