CREATE DATABASE IF NOT EXISTS beverage;

USE beverage;

CREATE TABLE IF NOT EXISTS pop (
    id integer PRIMARY KEY,
    name text NOT NULL,
    color text NOT NULL
);

GRANT ALL ON DATABASE beverage TO root;
