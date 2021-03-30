Drop EXTENSION if exists pgcrypto;
CREATE EXTENSION pgcrypto;
SET TIMEZONE TO 'Europe/Lisbon';

DROP TABLE IF exists users;
CREATE TABLE users
(
    id SERIAL PRIMARY KEY,
    username VARCHAR NOT NULL UNIQUE,
    firstName VARCHAR NOT NULL,
    lastName VARCHAR NOT NULL,
    password VARCHAR NOT NULL,
    created_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP
);


Insert into users (username,firstname,lastname, password) VALUES ('admin', 'admin', 'admin', crypt('admin', gen_salt('bf')));

 /*
SELECT currval(pg_get_serial_sequence('users', 'id'));
 
SELECT * from users;
*/
