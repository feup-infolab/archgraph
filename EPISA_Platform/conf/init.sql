CREATE EXTENSION IF NOT EXISTS pgcrypto;
SET TIMEZONE TO 'Europe/Lisbon';

CREATE TABLE IF NOT EXISTS users
(
    id SERIAL PRIMARY KEY,
    username VARCHAR NOT NULL UNIQUE,
    firstName VARCHAR NOT NULL,
    lastName VARCHAR NOT NULL,
    role VARCHAR NOT NULL,
    password VARCHAR NOT NULL,
    created_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP
);


Insert into users (username, firstname, lastname,role, password) VALUES ('admin', 'admin', 'admin', 'admin', crypt('admin', gen_salt('bf')));

Insert into users (username, firstname, lastname,role, password) VALUES ('user', 'user', 'user', 'user', crypt('user', gen_salt('bf')));

-- SELECT currval(pg_get_serial_sequence('users', 'id'));

-- SELECT * from users;
