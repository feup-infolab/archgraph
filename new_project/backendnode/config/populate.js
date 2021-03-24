(async () => {

    const path = require('path');
    const basename = path.basename(__filename);
    const env = process.env.NODE_ENV || 'development';
    const config = require(__dirname + '/../config/config.js')[env];
    const db = {};
    const Sequelize = require('sequelize');

    let sequelize;
    if (config.use_env_variable) {
        sequelize = new Sequelize(process.env[config.use_env_variable], config);
    } else {
        sequelize = new Sequelize(config.database, config.username, config.password, config);
    }
    const User = require('../models').User;
    await User.create({
        username: "olza",
        password: "a",
        firstName: "as",
        lastName: "asas",
    });
})();

