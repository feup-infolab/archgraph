// (async () => {
'use strict';

const fs = require('fs');
const path = require('path');
const basename = path.basename(__filename);
let env;
const myArgs = process.argv.slice(2);
if (myArgs.length > 0) {
    env = myArgs[0]
}
const config = require(__dirname + '/../config/config.js')[env];
const db = {};
const Sequelize = require('sequelize');
let sequelize;
sequelize = new Sequelize(config.db, config.username, config.password, config);
fs
    .readdirSync(__dirname)
    .filter(file => {
        return (file.indexOf('.') !== 0) && (file !== basename) && (file.slice(-3) === '.js');
    })
    .forEach(file => {
        const model = require(path.join(__dirname, file))(sequelize, Sequelize.DataTypes);
        db[model.name] = model;
    });

Object.keys(db).forEach(modelName => {
    if (db[modelName].associate) {
        db[modelName].associate(db);
    }
});

db.Sequelize = Sequelize;

console.log("All models were synchronized successfully.");
sequelize.sync()

module.exports = db;
// })();
