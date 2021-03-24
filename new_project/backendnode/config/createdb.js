(async () => {

    const client = require('pgtools');

    const dbName = process.env.DB_NAME || "db";

    try {
        await client.createdb({
            host: process.env.DB_HOST,
            port: process.env.DB_PORT,
            user: 'admin',
            password: 'admin',
        }, dbName);
    } catch (e) {
        console.log("database already exists")
        // Deal with the fact the chain failed
    }
})();
