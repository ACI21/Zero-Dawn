CREATE TABLE usuario(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(50) NOT NULL
);

CREATE TABLE caja (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre VARCHAR(255) NOT NULL UNIQUE,
    descripcion VARCHAR(255) NOT NULL UNIQUE,
    pista VARCHAR(255) NOT NULL,
    intentos INTEGER(2)
);

INSERT INTO usuario (username, password) VALUES('Ruthy','Billie Eilish');
INSERT INTO usuario (username, password) VALUES('admin','123');