CREATE TABLE materias (
    id uuid PRIMARY KEY,
    id_user uuid NOT NULL,
    nome VARCHAR(255)
);

CREATE TABLE users (
    id uuid PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    email VARCHAR(255) NOT NULL UNIQUE,
    senha_hash TEXT NOT NULL
);

CREATE TABLE topicos (
    id uuid PRIMARY KEY,
    id_materia uuid NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    prazo DATE
);

ALTER TABLE materias
ADD CONSTRAINT fk_user FOREIGN KEY (id_user) REFERENCES users(id);

ALTER TABLE topicos
ADD CONSTRAINT fk_materia FOREIGN KEY (id_materia) REFERENCES materias(id);