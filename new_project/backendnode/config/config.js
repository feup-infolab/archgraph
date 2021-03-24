require('dotenv').config();
const {DB_HOST, DB_PASSWORD, DB_USERNAME} = process.env
module.exports = {
    "development": {
        "username": 'admin',
        "password": 'admin',
        "database": "db",
        "host": '127.0.0.1',
        "port": 5432,
        "dialect": "postgres"
    },
    "test": {
        "username": DB_USERNAME,
        "password": DB_PASSWORD,
        "database": "db",
        "host": DB_HOST,
        "port": 5432,
        "dialect": "postgres"
    },
    "production": {
        "username": DB_USERNAME,
        "password": DB_PASSWORD,
        "database": "db",
        "host": DB_HOST,
        "port": 5432,
        "dialect": "postgres"
    }
}
