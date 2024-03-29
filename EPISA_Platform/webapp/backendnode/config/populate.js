async function populate() {
    var env;
    var myArgs = process.argv.slice(2);
    if (myArgs.length > 0) {
        env = myArgs[0]
    } else {
        env = "development"
    }
    const config = require(__dirname + '/config.js')[env];
    const Sequelize = require('sequelize');

    let sequelize;
    sequelize = new Sequelize(config.database, config.username, config.password, config);
    const Users = require('../models/users')(sequelize, Sequelize);


    try {
        await Users.create({
            username: 'admin',
            firstname: 'admin',
            lastname: 'admin',
            role: 'admin',
            password: 'admin',

        });
        await Users.create({
            username: 'user',
            firstname: 'user',
            lastname: 'user',
            role: 'user',
            password: 'user',
        });
        console.log("Admin added to the database")
    } catch (e) {
        console.log("Admin already exists into database")
    }
}

populate()
