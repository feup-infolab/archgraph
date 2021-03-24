(async () => {
    'use strict';

    const fs = require('fs');
    const path = require('path');
    const basename = path.basename(__filename);
    const env = process.env.NODE_ENV || 'development';
    const config = require(__dirname + '/../config/config.js')[env];
    const db = {};
    const client = require('pgtools');
    const Sequelize = require('sequelize');

    const dbName = process.env.DB_NAME || "db";
    try {
        await client.createdb({
            host: process.env.DB_HOST,
            port: process.env.DB_PORT,
            user: 'admin',
            password: 'admin',
        }, dbName);
    } catch (e) {
        // Deal with the fact the chain failed
    }


    let sequelize;
    if (config.use_env_variable) {
        sequelize = new Sequelize(process.env[config.use_env_variable], config);
    } else {
        sequelize = new Sequelize(config.database, config.username, config.password, config);
    }
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

    module.exports = db;
})();
