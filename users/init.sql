CREATE DATABASE users;
CREATE USER maksim with password 'deathless33';
GRANT ALL PRIVILEGES ON DATABASE users to maksim;
\c users;
CREATE TABLE IF NOT EXISTS users (id SERIAL primary key,username VARCHAR unique,
email VARCHAR unique,password VARCHAR,permission_id INT);
CREATE TABLE IF NOT EXISTS permissions (id SERIAL primary key,rights VARCHAR );

INSERT INTO permission (rights) values ('superuser'),('read_only') ON CONFLICT DO NOTHING;
INSERT INTO users (username,email,password,permission_id)
values ('maksim','maxim@gmail.com',crypt('123456',gen_salt('bf')),1) ON CONFLICT DO NOTHING;
INSERT INTO users (username,email,password,permission_id)
values ('alexey','alexey@gmail.com',crypt('123456',gen_salt('bf')),2) ON CONFLICT DO NOTHING;
