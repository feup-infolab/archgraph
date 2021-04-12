require('dotenv').config();
module.exports = {
    "development": {
        "username": 'admin',
        "password": 'admin',
        "database": "postgres",
        "host": '127.0.0.1',
        "port": 5432,
        "my_port": 8010,
        "dialect": 'postgres',
        "secret": 'IHaveASecurePassword'
    },
    "test": {
        "username": 'admin',
        "password": 'admin',
        "database": "postgres",
        "host": '127.0.0.1',
        "port": 5432,
        "my_port": 8010,
        "dialect": 'postgres',
        "secret": 'IHaveASecurePassword'
    },
    "production": {
        "username": 'admin',
        "password": 'admin',
        "database": "postgres",
        "host": 'postgres',
        "port": 5432,
        "my_port": 8010,
        "dialect": 'postgres',
        "secret": 'IHaveASecurePassword'
    }
}
