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