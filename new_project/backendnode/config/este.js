const client = require('pgtools');

const dbName = process.env.DB_NAME || "db";

client.createdb({
    host: process.env.DB_HOST,
    port: process.env.DB_PORT,
    user: 'admin',
    password: 'admin',
}, dbName, function (err, res) {
    if (err) {
        console.error(err);
        process.exit(-1);
    }
    console.log(res);
});
