-- Criar usuário da aplicação
CREATE USER app_user WITH PASSWORD 'VgY830HExnSC';

-- Dar acesso ao banco
GRANT CONNECT ON DATABASE app_db TO app_user;

-- Conectar no banco
\c app_db

-- Permissões no schema public
GRANT USAGE ON SCHEMA public TO app_user;

-- Permissões nas tabelas existentes
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO app_user;

-- Permissões para futuras tabelas
ALTER DEFAULT PRIVILEGES IN SCHEMA public
GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO app_user;