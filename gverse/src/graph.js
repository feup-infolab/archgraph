"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const gverse_1 = require("gverse");
class DBConnection {
    static getDatabase() {
        if (!DBConnection.graph) {
            DBConnection.graph = new gverse_1.default.Graph(new gverse_1.default.Connection({ host: "localhost", port: 9080 }));
        }
        return DBConnection.graph;
    }
}
module.exports.DBConnection = DBConnection;
//# sourceMappingURL=graph.js.map