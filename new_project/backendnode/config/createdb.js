(async () => {
    const client = require('pgtools');
    let env;
    const myArgs = process.argv.slice(2);
    if (myArgs.length > 0) {
        env = myArgs[0]
    }
    const config = require(__dirname + '/config.js')[env];

    try {
        await client.createdb({
            host: config.host,
            port: config.port,
            user: config.username,
            password: config.password,
        }, config.database);
    } catch (e) {
        console.log("database already exists")
        // Deal with the fact the chain failed
    }
})();
